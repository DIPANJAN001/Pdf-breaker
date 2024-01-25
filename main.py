import json
import fitz  # PyMuPDF

def structure_pdf_text(pdf_path):
    structure = {"sections": []}
    current_section = {"text": ""}

    with fitz.open(pdf_path) as pdf_doc:
        for page_num in range(pdf_doc.page_count):
            page = pdf_doc[page_num]
            text = page.get_text()

            for line in text.split('\n'):
                if line.strip():  # Skip empty lines
                    current_section["text"] += line.strip() + ' '
                else:
                    if current_section["text"]:
                        structure["sections"].append(current_section)
                        current_section = {"text": ""}

    return structure

# Example usage
pdf_path = 'IJETTCS-2019-10-11-10.pdf'  # Replace with the actual path to your PDF file
pdf_structure = structure_pdf_text(pdf_path)

# Dump the structured JSON as a file
with open('output_structure.json', 'w', encoding='utf-8') as json_file:
    json.dump(pdf_structure, json_file, ensure_ascii=False, indent=2)

print("Structured PDF text dumped to 'output_structure.json'")

