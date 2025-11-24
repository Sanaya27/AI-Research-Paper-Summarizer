# 🌟 AI Research Paper Summarizer

*A powerful Gemini-AI based tool to analyze, summarize, and extract insights from research papers.*

<p align="center">
  <img src="https://img.shields.io/badge/Framework-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/AI-Google%20Gemini-6f42c1?style=for-the-badge&logo=google&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
</p>

---

## 🚀 Overview

**AI Research Paper Summarizer** is a clean, modern and intelligent PDF-analysis tool powered by **Gemini 2.0 Flash**.  
It extracts structured knowledge from academic papers with just one click.  
Perfect for students, researchers, engineers, and literature-review workflows.

### ✨ Key Features
- 📝 **AI Summaries** (Short • Medium • Long, 5 different styles)
- 🎯 **Semantic Question Answering** from the PDF
- 🔍 **Title & Keyword Extraction**
- 🕵️ **Plagiarism & Originality Detection**
- 🧮 **Equation & Algorithm Extraction**
- 📊 **Auto-Generated PPT**
- 📄 **Research Notes PDF Export**
- 🌗 **Light / Dark Mode UI**
- ⚡ Fast, accurate and elegant UI built with **Streamlit**

---

## 🗂️ Project Flowchart
<img width="4624" height="2884" alt="diagram (2)" src="https://github.com/user-attachments/assets/c49f0b5a-b13b-4222-b7cc-fbbe0399306d" />

## 🗂️ Project Structure

```
📦 Research-Paper-Summarizer
├── app.py
├── summarizer.py
├── pdf_utils.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/Research-Paper-Summarizer.git
cd Research-Paper-Summarizer
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Add Your Gemini API Key
Create:

```
.streamlit/secrets.toml
```

Add:
```toml
GEMINI_API_KEY = "your_api_key_here"
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. Upload a research paper (PDF)  
2. The app extracts raw text  
3. Gemini processes and generates:
   - summaries  
   - keywords  
   - equations  
   - plagiarism insights  
   - structured data for PPT / PDF  
4. You can download:
   - 📥 Summary (TXT)  
   - 📥 Generated Presentation (PPTX)  
   - 📥 Research Notes (PDF)

---

## 📊 Screenshots

><img width="2556" height="1263" alt="image" src="https://github.com/user-attachments/assets/1de64490-8569-448a-80c2-ce5453cf60dc" />
<img width="2559" height="1264" alt="image" src="https://github.com/user-attachments/assets/b6fb3c80-2438-4de1-a8dc-2912cfc6b191" />
<img width="2558" height="1261" alt="image" src="https://github.com/user-attachments/assets/d4b141ec-72d7-409f-bd69-503ecd78cff1" />



---

## 📦 Deployment (Streamlit Cloud)

1. Push project to GitHub  
2. Go to **share.streamlit.io**  
3. Connect repo → select `app.py`  
4. Add secrets under **App Settings → Secrets**  
5. Deploy 🎉

---

## 📝 License
This project is licensed under the **MIT License**.

---

## 💙 Acknowledgements
- Google Gemini AI  
- Python-pptx  
- ReportLab  
- Streamlit  
- Open-Source Community  

---

## ⭐ Support
If you liked this project — **star the repo** ⭐  
Your support motivates further improvements!

