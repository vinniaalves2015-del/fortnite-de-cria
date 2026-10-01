from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Fortnite de Cria</title>
    </head>
    <body>
        <h1>🎮 FORTNITE DE CRIA</h1>
        <h2>🔥 BORA JOGAR!</h2>

        <p>🟢 Servidor online</p>
        <p>🐳 Rodando em Docker</p>

        <button>BORA JOGAR</button>
    </body>
    </html>
    """

app.run(host="0.0.0.0", port=8080)