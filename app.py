from flask import Flask, render_template, request, session, redirect, url_for
from models.personagem import Personagem
from models.classe import CLASSES_DISPONIVEIS
from models.raca import RACAS_DISPONIVEIS
import models.geracao_atributos as geracao_atributos

app = Flask(__name__)
# Chave secreta necessária para que as sessões funcionem
app.secret_key = 'sua_chave_secreta_muito_segura_aqui'


@app.route("/", methods=["GET", "POST"])
def index():
    """Página inicial para a criação do personagem."""
    if request.method == "POST":
        # Salva os IDs de classe e raça na sessão do usuário
        session['nome'] = request.form["nome"]
        session['id_classe'] = request.form["classe"]
        session['id_raca'] = request.form["raca"]

        return redirect(url_for('escolher_atributos'))

    return render_template("index.html", classes=CLASSES_DISPONIVEIS, racas=RACAS_DISPONIVEIS)


@app.route("/atributos", methods=["GET", "POST"])
def escolher_atributos():
    """Página para escolher o modo de rolagem de atributos."""
    if 'nome' not in session:
        return redirect(url_for('index'))  # Redireciona se os dados básicos não existirem

    if request.method == "POST":
        modo = request.form.get("modo")
        atributos_finais = {}
        if modo == "1":
            atributos_finais = geracao_atributos.gerar_atributos_classico()
        elif modo in ["2", "3"]:
            if modo == "2":
                atributos_finais = list(geracao_atributos.gerar_atributos_heroico())
            else: 
                atributos_finais = list(geracao_atributos.gerar_atributos_aventureiro())
        else:
            atributos_finais = geracao_atributos.gerar_atributos_classico()

        
        classe_obj = CLASSES_DISPONIVEIS[session['id_classe']]
        raca_obj = RACAS_DISPONIVEIS[session['id_raca']]

        # Cria a instância do personagem passando os objetos
        heroi = Personagem(
            nome=session['nome'],
            classe=classe_obj,
            raca=raca_obj
        )
        heroi.atributos = atributos_finais

        # Armazena o herói na sessão usando o método to_dict()
        session['heroi'] = heroi.to_dict()

        return redirect(url_for('mostrar_personagem'))

    return render_template("atributos.html")


@app.route("/personagem")
def mostrar_personagem():
    """Página para exibir a ficha completa do personagem."""
    heroi_data = session.get('heroi')
    if not heroi_data:
        return redirect(url_for('index'))

    # Usa diretamente os dados serializados
    heroi_para_exibir = {
        'nome': heroi_data['nome'],
        'classe': heroi_data['classe']['nome'],
        'raca': heroi_data['raca']['nome'],
        'nivel': heroi_data['nivel'],
        'vida': heroi_data['vida'],
        'xp': heroi_data['xp'],
        'atributos': heroi_data['atributos']
    }

    return render_template("personagem.html", heroi=heroi_para_exibir)


if __name__ == "__main__":
    app.run(debug=True)
