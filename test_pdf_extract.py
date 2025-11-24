from pdf_utils import extract_text_from_pdf
import os

file_path = "backend/sample_research_paper.pdf"
# Full path to your file

if os.path.exists(file_path):
    text = extract_text_from_pdf(file_path)
    if text.strip():
        print("✅ PDF Text Extracted:\n")
        print(text[:1000])  # First 1000 characters
    else:
        print("⚠️ PDF has no extractable text (maybe it's scanned?)")
else:
    print(f"❌ File not found: {file_path}")
