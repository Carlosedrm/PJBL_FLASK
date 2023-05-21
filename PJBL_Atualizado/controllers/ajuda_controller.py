from re import template
from flask import Blueprint, render_template,redirect,url_for,request, flash
from models import db, Conserto, Solucao, Reclamacao, Vaga

ajuda = Blueprint("ajuda", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

@ajuda.route("/")
def ajuda_index():
    return render_template("/ajuda/Ajuda.html")

@ajuda.route("/conserto")
def conserto_index():
    vagas = Vaga.query.all()
    return render_template("/ajuda/Conserto.html", vaga = vagas)

@ajuda.route("/reclamacao")
def reclamacao_index():
    return render_template("/ajuda/Reclamacao.html")

@ajuda.route("/solucao")
def solucao_index():
    return render_template("/ajuda/Solucao.html")

# Recolher as informações

@ajuda.route("/conserto_geral", methods=["POST","GET"])
def conserto_geral():
    if request.method == "POST":
        numero_vaga = request.form["numero_vaga"]
        descricao = request.form["descricao"]

    new_conserto = Conserto(numero_vaga = numero_vaga, descricao  = descricao)
    db.session.add(new_conserto)
    db.session.commit()

    return redirect(url_for("ajuda.listar_consertos"))

@ajuda.route("/reclamacao_relato", methods=["POST","GET"])
def reclamacao_relato():
    if request.method == "POST":
        reclamacao = request.form["reclamacao"]
        titulo = request.form["titulo"]

    new_reclamacao = Reclamacao(titulo = titulo, descricao = reclamacao)
    db.session.add(new_reclamacao)
    db.session.commit()

    return redirect(url_for("ajuda.listar_reclamacoes"))

# Listagem das informações

@ajuda.route("/listar_consertos")
def listar_consertos():
    consertos = Conserto.query.all()
    return render_template("ajuda/ListarConserto.html", conserto = consertos)

@ajuda.route("/listar_reclamacoes")
def listar_reclamacoes():
    reclamacoes = Reclamacao.query.all()
    return render_template("ajuda/ListarReclamacao.html", reclamcacao = reclamacoes)

# Para a alteração de informações

@ajuda.route("/delete_conserto/<id>")
def delete_conserto(id):
    if Conserto.delete_conserto(id):
        flash("Essa entrada de conserto foi excluida com sucesso!", "success")
    else:
        flash("Algo deu errado!", "danger")
    return redirect(url_for("ajuda.listar_consertos"))

@ajuda.route("/update_conserto/<id>")
def update_conserto(id):
    conserto = db.session.query(Conserto).filter(Conserto.id == int(id)).first()
    vagas = Vaga.query.all()
    return render_template("/ajuda/AtualizarConserto.html", conserto = conserto, vaga = vagas)

@ajuda.route("/save_conserto_changes", methods = ["POST"])
def save_conserto_changes():
    data = request.form.copy()
    Conserto.update_conserto(data)
    return redirect(url_for("ajuda.listar_consertos"))

# Para a alteração das reclamações

@ajuda.route("/delete_reclamacao/<id>")
def delete_reclamacao(id):
    if Reclamacao.delete_reclamacao(id):
        flash("Essa reclamação foi excluida com sucesso!", "success")
    else:
        flash("Algo deu errado!", "danger")
    return redirect(url_for("ajuda.listar_reclamacoes"))

# Para chamadas solucionadas

@ajuda.route("/listar_solucao")
def listar_solucao():
    solucoes = Solucao.query.all()
    return render_template("/ajuda/Solucao.html", solucao = solucoes)


@ajuda.route("/save_solucao/<id>")
def save_solucao(id):
    conserto = db.session.query(Conserto).filter(Conserto.id == int(id)).first()
    
    new_solucao = Solucao(numero_vaga = conserto.numero_vaga, descricao = conserto.descricao)
    db.session.add(new_solucao)
    db.session.commit()

    # Remove o conserto da tabela
    Conserto.delete_conserto(id)
    return redirect(url_for("ajuda.listar_solucao"))

