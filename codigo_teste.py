import pypdf
import ollama
import pandas as pd


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

# Função para organizar o texto em uma estrutura tabular (DataFrame)
def organize_text_to_table(text):
    # Aqui você pode definir como quer organizar os dados.
    # Por exemplo, se o PDF tiver seções claras, você pode dividir o texto com base em padrões.
    # Vou criar um exemplo simples onde cada linha do PDF vira uma linha na planilha.
    
    # Divide o texto em linhas
    lines = text.split('\n')
    
    # Cria um DataFrame com uma coluna chamada "Conteúdo"
    df = pd.DataFrame(lines, columns=["Conteúdo"])
    
    return df

# Função para salvar o DataFrame em uma planilha Excel
def save_to_excel(df, output_file):
    df.to_excel(output_file, index=False)
    print(f"Planilha salva em: {output_file}")

# Organizar o texto em uma tabela
df = organize_text_to_table(texto)

# Salvar a tabela em uma planilha Excel
output_file = "conteudo_pdf.xlsx"
save_to_excel(df, output_file)