import requests

print("================================")
print("       🤖 duster-x             ")
print("================================")
print()
print("Digite sua pergunta.")
print("Para sair, digite: sair")
print()

while True:
    pergunta = input("Você: ")

    if pergunta.lower() == "sair":
        print("Até mais!")
        break

    resposta = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "qwen3:4b",
            "messages": [
                {
                    "role": "user",
                    "content": pergunta
                }
            ],
            "stream": False
        }
    )

    dados = resposta.json()

    print()
    print("IA:", dados["message"]["content"])
    print()