from flask import Flask, render_template, request, session, redirect, url_for
from models.personagem import Personagem
from models.classe import CLASSES_DISPONIVEIS
from models.raca import RACAS_DISPONIVEIS
import models.geracao_atributos as geracao_atributos

app = Flask(__name__)
# Chave secreta necessária para que as sessões funcionem
app.secret_key = 'sunga_branca'


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
    
    if 'nome' not in session:
        return redirect(url_for('index'))  # Redireciona se os dados básicos não existirem

    if request.method == "POST":
        modo = request.form.get("modo")
        
        # Modo Clássico cria o personagem diretamente
        if modo == "1":
            atributos = geracao_atributos.gerar_atributos_classico()
            
            classe_obj = CLASSES_DISPONIVEIS[session["id_classe"]]
            raca_obj = RACAS_DISPONIVEIS[session["id_raca"]]

            heroi = Personagem(
                nome=session["nome"],
                classe=classe_obj,
                raca=raca_obj,
            )
            heroi.atributos = atributos
            session["heroi"] = heroi.to_dict()
            return redirect(url_for("mostrar_personagem"))

        # Outros modos redirecionam para a distribuição
        elif modo == "2":  # heróico
            valores = geracao_atributos.gerar_atributos_heroico()
        elif modo == "3":  # aventureiro
            valores = geracao_atributos.gerar_atributos_aventureiro()
        else: # Se nenhum modo for selecionado, volta
            return redirect(url_for("escolher_atributos"))

        session["valores"] = valores
        session["modo_atributos"] = modo
        return redirect(url_for("distribuir_atributos"))

    return render_template("atributos.html")


@app.route("/distribuir", methods=["GET", "POST"])
def distribuir_atributos():
    valores = session.get("valores")
    modo = session.get("modo_atributos")

    if not valores:
        return redirect(url_for("escolher_atributos"))

    atributos_nomes = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]

    if request.method == "POST":
        valores_usados = [int(v) for v in request.form.values()]
        if sorted(valores_usados) != sorted(valores):
            # Adicionar uma mensagem de erro aqui seria ideal
            return redirect(url_for('distribuir_atributos'))

        atributos_finais = {}
        for nome in atributos_nomes:
            escolha = request.form.get(nome)
            if escolha:
                atributos_finais[nome] = int(escolha)

        # Cria personagem
        classe_obj = CLASSES_DISPONIVEIS[session["id_classe"]]
        raca_obj = RACAS_DISPONIVEIS[session["id_raca"]]

        heroi = Personagem(
            nome=session["nome"],
            classe=classe_obj,
            raca=raca_obj,
        )
        heroi.atributos = atributos_finais
        session["heroi"] = heroi.to_dict()

        # Limpa os dados temporários da sessão
        session.pop("valores", None)
        session.pop("modo_atributos", None)

        return redirect(url_for("mostrar_personagem"))

    return render_template("distribuir.html", valores=valores, atributos=atributos_nomes, modo=modo)


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