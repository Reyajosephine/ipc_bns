#  IPC ↔ BNS Comparator

This project helps you compare legal sections from the **Indian Penal Code (IPC)** with their updated versions in the **Bharatiya Nyaya Sanhita (BNS)** using AI.

# What are IPC and BNS?

- **IPC** (Indian Penal Code):  
  Introduced in 1860, it was India’s main criminal law for over 160 years. It defines crimes like theft, murder, cheating, etc., and their punishments.

- **BNS** (Bharatiya Nyaya Sanhita):  
  Passed in 2023, BNS replaces IPC as part of a major criminal law overhaul in India. It includes updated language, restructured sections, and new definitions for certain offenses.

You just enter an IPC section number (like `420`), and the app:
- Finds the most similar section in BNS
- Highlights what changed (punishment, fines, wording)
- Uses an AI model to explain the differences in plain English

---

##  Why this project?

India recently replaced its criminal laws:
- **IPC → BNS**
- **CrPC → BNSS**
- **IEA → BSA**

But there’s no official one-to-one mapping between old and new sections. This tool makes it easier to:
- Learn what's changed
- Understand updates quickly
- Avoid legal confusion during the transition

---

##  Features

-  Enter an IPC section number and get the matching BNS section
-  See word-by-word changes in law descriptions
-  Get summaries of punishment/fine updates
- AI-powered explanation using **Gemma-2B-it** (runs on CPU)
-  Clean web interface using Streamlit

---

##  Tech Stack

| Tool | Why it’s used |
|------|---------------|
| Python | Core language |
| Streamlit | Web UI |
| Hugging Face Transformers | Loads AI model |
| Gemma-2B-it | Generates plain-language summaries |
| difflib | Compares legal text |
| regex | Extracts fine/punishment data |
| JSON | Stores IPC and BNS sections |

---

## Project Structure


```bash
├── app.py               # Streamlit UI
├── compare.py           # Matching + change detection logic
├── llm_model.py         # LLM text generation
├── ipc_sections.json    # IPC section data
├── bns_sections.json    # BNS section data
├── requirements.txt     # Python packages
└── README.md            # You’re here!
```

How to Run
1. Clone the repo
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
3. Set up virtual environment (optional but recommended)
```bash
python -m venv venv
.\venv\Scripts\activate       # Windows
source venv/bin/activate     # macOS/Linux
```
4. Install dependencies
```bash
pip install -r requirements.txt
```
5. Run the app
```bash
streamlit run app.py
```
Then open http://localhost:8501 in your browser.

Example Use
Input:
420

Output:
```bash
--Matching BNS section
--Similarity score: 88.6%
--Fine changed from ₹5000 to ₹10000
--AI explanation of real-world impact
```
# Limitations: 
This is not a legal advice tool.
Matching is based on text similarity, not official cross-references.
Some AI explanations may be simplified.

# Future Plans
Add CrPC ↔ BNSS and IEA ↔ BSA comparison
Improve section matching using sentence embeddings
Add multi-language support (Hindi, Tamil, etc.)
Deploy online

# Acknowledgements
Hugging Face
Google Gemma-2B-it model
Official Gazette of India

# License
MIT — use it, modify it, improve it. Credit is appreciated.

# Output:
![WhatsApp Image 2025-08-08 at 13 50 43_6d35e527](https://github.com/user-attachments/assets/33ebf97d-ee0c-4a43-b001-f8a012e5584d)
![WhatsApp Image 2025-08-08 at 13 51 06_e4e3ea77](https://github.com/user-attachments/assets/75c99027-7d70-4004-8b36-04425a7d835f)
![WhatsApp Image 2025-08-08 at 13 51 22_babb6bab](https://github.com/user-attachments/assets/2b23745e-3852-48b4-b062-cc66cf608976)




