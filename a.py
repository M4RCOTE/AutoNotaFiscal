import ollama

response = ollama.chat(model='deepseek-r1:1.5b', messages=[
    {
        'role': 'user',
        'content': f'Why is the sky blue?',
    },
])

print(response['message']['content'])