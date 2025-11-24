import fitz  
import os

def extract_text_from_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return

    doc = fitz.open(pdf_path)
    full_text = ""

    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        full_text += f"--- Page {page_num + 1} ---\n{text}\n"

    doc.close()
    return full_text

if __name__ == "__main__":
    input_pdf = "sample.pdf"  
    extracted_text = extract_text_from_pdf(input_pdf)

    if extracted_text:
        with open("extracted_text.txt", "w", encoding="utf-8") as f:
            f.write(extracted_text)
        print("Text extraction complete. Saved to 'extracted_text.txt'.")
from llm_infer import summarize_text
summary = summarize_text(extracted_text)
if summary:
    with open("summary.txt", "w", encoding="utf-8") as sfile:
        sfile.write(summary)
    print("Summary saved to 'summary.txt'")
else:
    print(" Could not generate summary.")
    
