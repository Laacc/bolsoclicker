from flask import Flask, render_template, redirect, url_for
from logic import GerenciarJogo

app = Flask(__name__)
jogo = GerenciarJogo()

@app.route("/")
def pagina_inicial():
    return render_template("index.html", pontos=jogo.pontos_totais, pps=jogo.pontos_passivos, ppc=jogo.valor_clique)

@app.route("/clicar",methods=["POST"])
def clicar():
    jogo.add_pontos()
    return redirect(url_for("pagina_inicial"))

@app.route("/salvar",methods=["POST"])
def salvar():
    jogo.salvar_jogo()
    return redirect(url_for("pagina_inicial"))

@app.route("/comprar/<id_item>",methods=["POST"])
def comprar(id_item):
    jogo.comprar_upgrade(id_item)
    return redirect(url_for("pagina_inicial"))


if __name__ == "__main__":
    app.run(debug=True)