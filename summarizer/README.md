# Research Paper Summarizer using Google Gemini

Automatically extract and summarize research papers (PDFs) using Google's Gemini 1.5 Pro LLM.  
Built with simplicity, speed, and clean NLP integration in mind.

---

## Features

- Extracts raw text from academic/research PDFs.
- Generates concise summaries using Gemini 1.5 Pro via API.
- Outputs full extracted text and LLM-generated summary to local `.txt` files.
- Gemini API integration with `.env` security.

---

## Folder Structure

```
Research-Paper-Summarizer

├── main.py               # Main runner script
├── llm_infer.py          # Handles Gemini LLM integration
├── sample.pdf            # Your input PDF (can be renamed)
├── extracted_text.txt    # Output: extracted full text
├── summary.txt           # Output: summary from LLM
├── requirements.txt      # Python dependencies
├── .env                  # API key (NOT to be pushed!)
└── README.md             # This file
```

---

## How It Works

1. Upload any research paper in PDF format.
2. The script:
   - Extracts and cleans the text.
   - Sends it to Gemini 1.5 Pro API.
   - Writes the summary and original text into `summary.txt` and `extracted_text.txt`.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Sanaya27/Research-Paper-Summarizer.git
cd Research-Paper-Summarizer
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate     # For Windows
# OR
source .venv/bin/activate  # For macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Get Your Google Gemini API Key

- Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
- Copy your API key and add it to a `.env` file:

```
GEMINI_API_KEY=your-api-key-here
```

Note: Never share your `.env` file or expose API keys in code.

---

## Run the Script

Make sure you have a PDF file (e.g., `sample.pdf`) in the root directory, then:

```bash
python main.py
```

**Outputs:**
- `extracted_text.txt` → Full content from the PDF
- `summary.txt` → Gemini-generated summary

---

## Customizing Output Length

You can change the summary length or level of detail by modifying prompts in `llm_infer.py`.

---

## Environment Variables

| Variable         | Description               |
|------------------|---------------------------|
| `GEMINI_API_KEY` | Your Gemini API Key       |

Use a `.env` file to store it safely:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Troubleshooting

- 404 Errors: You may be using a wrong model name or incorrect API version.
- Quota Exceeded: You're likely hitting free-tier limits. Check usage: https://ai.google.dev/gemini-api/docs/rate-limits
- Not a git repo: Run `git init` before committing or pushing changes.

---

## Powered By

- PyMuPDF – PDF text extraction
- Google Generative AI – LLM-based summarization (Gemini 1.5 Pro)
- Python 3.10+
- dotenv – Secure environment variables

---

## Author

**Sanaya** – LLM Integration Specialist  
GitHub: [@Sanaya27](https://github.com/Sanaya27)  
Feedback / Collaboration: Open to suggestions and improvements

