import pypdf
import ollama

# Função para extrair texto de um PDF
def pdf_to_text(file_path):
    with open(file_path, 'rb') as file:
        reader = pypdf.PdfReader(file)
        text = ''

        for page in reader.pages:
            text += page.extract_text()

        return text

# Função para interagir com a IA 
def ask_ai(prompt, context):
    response = ollama.generate(
        model="deepseek-r1:1.5b",
        prompt=f"{prompt}\n\nContexto:\n{context}"
    )
    return response['response']

# Caminho do arquivo PDF
file_path = 'Curriculo-1.pdf'

# Extrair texto do PDF
texto = pdf_to_text(file_path)
print("Texto extraído do PDF:\n", texto)

# Interação com a IA
while True:
    user_input = input("\nPergunta para a IA: ")
    if user_input.lower() in ["sair", "exit"]:
        print("AI: Até logo!")
        break

    # Passa a pergunta do usuário e o texto do PDF como contexto para a IA
    resposta = ask_ai(user_input, texto)
    print(f"AI: {resposta}")