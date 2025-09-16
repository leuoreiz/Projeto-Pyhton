from flask import Flask, render_template, request
from personagem import Personagem

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form["nome"]
        classe = request.form["classe"]
        raca = request.form["raca"]

        # Cria o personagem com os dados do formulário
        heroi = Personagem(nome, classe, raca)

        return render_template("personagem.html", heroi=heroi)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
