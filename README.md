# ⚖ IPC ↔ BNS Comparator

This project helps you compare legal sections from the **Indian Penal Code (IPC)** with their updated versions in the **Bharatiya Nyaya Sanhita (BNS)** using AI.

You just enter an IPC section number (like `420`), and the app:
- Finds the most similar section in BNS
- Highlights what changed (punishment, fines, wording)
- Uses an AI model to explain the differences in plain English

---

## 🧠 Why this project?

India recently replaced its criminal laws:
- **IPC → BNS**
- **CrPC → BNSS**
- **IEA → BSA**

But there’s no official one-to-one mapping between old and new sections. This tool makes it easier to:
- Learn what's changed
- Understand updates quickly
- Avoid legal confusion during the transition

---

## 🚀 Features

- 🔍 Enter an IPC section number and get the matching BNS section
- ✂️ See word-by-word changes in law descriptions
- 📊 Get summaries of punishment/fine updates
- 🤖 AI-powered explanation using **Gemma-2B-it** (runs on CPU)
- 🌐 Clean web interface using Streamlit

---

## 🛠 Tech Stack

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

## 📁 Project Structure

```bash
.
├── app.py               # Streamlit UI
├── compare.py           # Matching + change detection logic
├── llm_model.py         # LLM text generation
├── ipc_sections.json    # IPC section data
├── bns_sections.json    # BNS section data
├── requirements.txt     # Python packages
└── README.md            # You’re here!

How to Run
1. Clone the repo
bash
Copy
Edit
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Set up virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
.\venv\Scripts\activate       # Windows
source venv/bin/activate     # macOS/Linux
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the app
bash
Copy
Edit
streamlit run app.py
Then open http://localhost:8501 in your browser.

🧪 Example Use
Input:
420

Output:

Matching BNS section

Similarity score: 88.6%

Fine changed from ₹5000 to ₹10000

AI explanation of real-world impact

⚠️ Limitations
This is not a legal advice tool.

Matching is based on text similarity, not official cross-references.

Some AI explanations may be simplified.

🧩 Future Plans
Add CrPC ↔ BNSS and IEA ↔ BSA comparison

Improve section matching using sentence embeddings

Add multi-language support (Hindi, Tamil, etc.)

Deploy online

📚 Acknowledgements
Hugging Face

Google Gemma-2B-it model

Official Gazette of India

📜 License
MIT — use it, modify it, improve it. Credit is appreciated.

yaml
Copy
Edit

---
##Output:
![WhatsApp Image 2025-08-08 at 13 50 43_b44b096c](https://github.com/user-attachments/assets/f1cdfb12-806f-40bc-80ab-68bf7cbbd2d2)
