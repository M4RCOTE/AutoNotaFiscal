import pypdf
import ollama

def pdf_to_text(file_path):
    with open(file_path, 'rb') as file:
        reader = pypdf.PdfReader(file)
        text = ''

        for page in reader.pages:
            text += page.extract_text()

        return text

file_path = 'Curriculo-1.pdf'

texto = pdf_to_text(file_path)
print(texto)