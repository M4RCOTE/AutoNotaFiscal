#codigo principal

import PyPDF2
import ollama

def pdf_to_text(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''

        for page in reader.pages:
            text += page.extract_text()

        return text

file_path = 'documento.pdf'

texto = pdf_to_text(file_path)
