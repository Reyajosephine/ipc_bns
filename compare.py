import json
import re
from difflib import SequenceMatcher
from sentence_transformers import SentenceTransformer
import numpy as np

from llm_model import generate_summary  # Import your llm_model generate_summary here

# Load JSON data
with open("ipc_sections.json", "r", encoding="utf-8") as f:
    ipc_data = json.load(f)

with open("bns_sections.json", "r", encoding="utf-8") as f:
    bns_data = json.load(f)

# SentenceTransformer retrieval model
retriever_model = SentenceTransformer('all-MiniLM-L6-v2')
bns_texts = [section['description'] for section in bns_data]
bns_embeddings = retriever_model.encode(bns_texts, convert_to_tensor=True)

def extract_legal_details(text):
    details = {
        "min_years": None,
        "max_years": None,
        "life_imprisonment": False,
        "fine": None,
        "special_conditions": []
    }
    years = re.findall(r"(\d+)\s*year", text.lower())
    if years:
        details["min_years"] = int(years[0])
        if len(years) > 1:
            details["max_years"] = int(years[1])
    if "life imprisonment" in text.lower() or "imprisonment for life" in text.lower():
        details["life_imprisonment"] = True
    fine_match = re.search(r"fine\s*(?:of)?\s*₹?\s?([\d,]+)", text)
    if fine_match:
        details["fine"] = fine_match.group(1)
    conditions = re.findall(r"\b(on|during|being|while)\s+[^.;,]+", text)
    details["special_conditions"] = [c.strip() for c in conditions]
    return details

def compare_details(ipc_details, bns_details):
    changes = []
    if ipc_details["min_years"] != bns_details["min_years"]:
        changes.append(f"Minimum imprisonment changed from {ipc_details['min_years'] or 'N/A'} years to {bns_details['min_years'] or 'N/A'} years.")
    if ipc_details["max_years"] != bns_details["max_years"]:
        changes.append(f"Maximum imprisonment changed from {ipc_details['max_years'] or 'N/A'} years to {bns_details['max_years'] or 'N/A'} years.")
    if ipc_details["life_imprisonment"] != bns_details["life_imprisonment"]:
        if bns_details["life_imprisonment"]:
            changes.append("Life imprisonment provision has been added.")
        else:
            changes.append("Life imprisonment provision has been removed.")
    if ipc_details["fine"] != bns_details["fine"]:
        changes.append(f"Fine changed from ₹{ipc_details['fine'] or 'N/A'} to ₹{bns_details['fine'] or 'N/A'}.")
    added_conditions = set(bns_details["special_conditions"]) - set(ipc_details["special_conditions"])
    removed_conditions = set(ipc_details["special_conditions"]) - set(bns_details["special_conditions"])
    if added_conditions:
        changes.append(f"New special conditions added: {', '.join(added_conditions)}.")
    if removed_conditions:
        changes.append(f"Special conditions removed: {', '.join(removed_conditions)}.")
    if not changes:
        changes.append("No major legal changes detected, mostly wording updates.")
    return changes

def keyword_overlap(title1, title2):
    words1 = set(re.findall(r"\w+", title1.lower()))
    words2 = set(re.findall(r"\w+", title2.lower()))
    if not words1 or not words2:
        return 0
    return len(words1 & words2) / len(words1 | words2)

def retrieve_candidates(ipc_desc, top_k=3):
    ipc_embedding = retriever_model.encode(ipc_desc, convert_to_tensor=True)
    cos_scores = (ipc_embedding @ bns_embeddings.T).cpu().numpy()
    top_indices = np.argsort(-cos_scores)[:top_k]
    return [bns_data[i] for i in top_indices], cos_scores[top_indices]

def find_best_match_with_changes(ipc_section_number):
    ipc_section = next((s for s in ipc_data if s["section"] == ipc_section_number), None)
    if not ipc_section:
        return {"error": f"IPC section {ipc_section_number} not found."}

    candidates, _ = retrieve_candidates(ipc_section["description"], top_k=3)

    best_match = None
    highest_score = 0

    for bns_section in candidates:
        desc_ratio = SequenceMatcher(None, ipc_section["description"], bns_section["description"]).ratio()
        title_score = keyword_overlap(ipc_section["title"], bns_section["title"])
        final_score = (0.7 * desc_ratio) + (0.3 * title_score)
        if final_score > highest_score:
            highest_score = final_score
            best_match = bns_section

    if not best_match:
        return {"error": "No matching BNS section found."}

    ipc_details = extract_legal_details(ipc_section["description"])
    bns_details = extract_legal_details(best_match["description"])
    changes = compare_details(ipc_details, bns_details)

    similarity_info = f"Best match similarity score: {round(highest_score * 100, 2)}%"

    llm_summary = generate_summary(ipc_section["description"], best_match["description"])

    return {
        "ipc_section": ipc_section,
        "bns_section": best_match,
        "similarity": similarity_info,
        "change_summary": changes,
        "llm_summary": llm_summary
    }
