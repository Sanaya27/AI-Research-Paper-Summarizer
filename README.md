# Research Paper Summarizer

A collaborative project that extracts and summarizes research papers using LLMs. The system is modular, team-driven, and leverages cutting-edge AI for summarization.

---

## 🔹 Project Overview

The **Research Paper Summarizer** is a Python-based solution that:
- Extracts textual data from PDF research papers
- Cleans and preprocesses the extracted text
- Summarizes it using a large language model (Gemini 1.5 Pro)
- Outputs both the raw and summarized content for easy consumption

---

## 🔹 Folder Structure

```
Research-Paper-Summarizer/
│
├── pdf-text-extractor-backend/        # Khushboo's component
│   ├── main.py
│   ├── llm_infer.py
│   ├── summary.txt
│   ├── extracted_text.txt
│   ├── requirements.txt
│   ├── sample.pdf
│   └── .env (ignored)
│
├── frontend/                          # Riya's component (placeholder)
│   └── (To be added)
│
├── integrations/                      # Sanaya & Himank
│   └── (Model API, backend linking)
│
├── datasets/                          # Anjika's component (placeholder)
│   └── (Research paper PDFs, metadata)
│
├── docs/                              # Yashvi's documentation
│   ├── architecture.md
│   ├── methodology.md
│   └── summary_flow.md
│
├── .gitignore
└── README.md                          # You’re reading it
```

---

## 🔹 Team Roles

| Name      | Role                              | Responsibility                                   |
|-----------|-----------------------------------|--------------------------------------------------|
| Sanaya    | LLM Integration & GitHub Maintainer | Connects backend with Gemini, manages repo       |
| Riya      | Frontend & UI Coordinator +  Integration Specialist       | Will design the frontend interface,integrates all components               |
| Yashvi    | Report & Documentation Lead       | Writes README, methodology, and documentation    |
| Anjika    | Research & Dataset Curator        | Finds research papers, prepares inputs           |
| Khushboo  | Backend Developer                 | Builds PDF extractor, text processor             |
| Himank    | Testing Specialist                | Tests final outputs                              |

---

## 🔹 Technologies Used

- **Python 3.11+**
- **Google Gemini API (gemini-1.5-pro)**
- **PyMuPDF (PDF text extraction)**
- **dotenv (secure API key handling)**
- **Git/GitHub (version control & collaboration)**
- **Streamlit**
- **Streamlit Cloud**

---

## 🔹 How to Run the Backend Locally

1. Clone the repo:
```bash
git clone https://github.com/Sanaya27/Research-Paper-Summarizer.git
```

2. Navigate to the backend folder:
```bash
cd Research-Paper-Summarizer/pdf-text-extractor-backend
```

3. Create and activate a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate   # for Windows
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Add your API key to a `.env` file:
```
GOOGLE_API_KEY=your_api_key_here
```

6. Run the backend:
```bash
python main.py
```

---

## 🔹 Contribution Guidelines

- Always pull before pushing:  
  `git pull origin main`

- Create a new branch if you're working on a feature:
  ```bash
  git checkout -b feature-branch-name
  ```

- Commit often with meaningful messages

- Do **not** upload your `.env` or local PDF files to the repo

---

## 🔹 License

This project is MIT Licensed.

---

Let’s build something impactful, together.

