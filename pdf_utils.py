import fitz  # PyMuPDF


def extract_text_from_pdf(file_path):
    """
    Extracts all text from a PDF file path and returns as a string.
    """
    doc = fitz.open(file_path)  # Open the PDF
    text = ""
    for page in doc:
        text += page.get_text()  # Extract text from each page
    doc.close()
    return text
