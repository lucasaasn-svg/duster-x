from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/perguntar", methods=["POST"])
def perguntar():
    dados = request.get_json()
    pergunta = dados.get("pergunta", "")

    if not pergunta:
        return jsonify({
            "resposta": "Digite uma pergunta."
        })

    resposta = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "qwen3:4b",
            "messages": [
                {
                    "role": "system",
                    "content": """
Você é uma IA escolar chamada duster-x.

Sua função é ajudar estudantes com Matemática,
Português, História, Geografia, Ciências, Inglês
e outras matérias.
o nome do seu criador e lucas benjamin
Explique os assuntos de maneira clara e didática.
Quando resolver exercícios, mostre os passos.
Se o estudante estiver aprendendo algo, explique
de forma simples antes de dar a resposta.

Nunca invente informações quando não tiver certeza.
"""
                },
                {
                    "role": "user",
                    "content": pergunta
                }
            ],
            "stream": False
        }
    )

    dados_resposta = resposta.json()

    return jsonify({
        "resposta": dados_resposta["message"]["content"]
    })


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)