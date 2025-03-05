import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """Extract text from a given PDF file."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    return text

# Example usage
pdf_path_1 = "Guide-to-Litigation-in-India.pdf"
pdf_path_2 = "Legal-Compliance-Corporate-Laws.pdf"

text_1 = extract_text_from_pdf(pdf_path_1)
text_2 = extract_text_from_pdf(pdf_path_2)

# Save extracted text for later processing
with open("litigation_text.txt", "w", encoding="utf-8") as f:
    f.write(text_1)

with open("corporate_laws_text.txt", "w", encoding="utf-8") as f:
    f.write(text_2)