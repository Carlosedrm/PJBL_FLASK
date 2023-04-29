from re import template
from flask import Blueprint, render_template,redirect,url_for,request

ajuda = Blueprint("ajuda", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

problema = []
problemas_de_seguraça = []
problema_reclamacao = []

@ajuda.route("/")
def ajuda_index():
    return render_template("/ajuda/Ajuda.html")

@ajuda.route("/conserto")
def conserto_index():
    return render_template("/ajuda/Conserto.html")

@ajuda.route("/seguranca")
def seguranca_index():
    return render_template("/ajuda/Seguranca.html")

@ajuda.route("/reclamacao")
def reclamacao_index():
    return render_template("/ajuda/Reclamacao.html")

@ajuda.route("/conserto_geral", methods=["POST","GET"])
def conserto_geral():
    if request.method == "POST":
        numero_vaga = request.form["numero_vaga"]
        descricao = request.form["descricao"]
    elif request.method == "GET":
        numero_vaga = request.args.get("numero_vaga")
        descricao = request.args.get("descricao")
    global problema
    problema.append(str(numero_vaga)+", "+str(descricao)+".")
    return redirect(url_for("ajuda.ajuda_index"))

@ajuda.route("/problema_seguranca", methods=["POST","GET"])
def problema_seguranca():
    if request.method == "POST":
        problema_de_seguranca = request.form["problema_de_seguranca"]
    elif request.method == "GET":
        problema_de_seguranca = request.args.get("problema_de_seguranca")
    global problemas_de_seguraça
    problemas_de_seguraça.append(str(problema_de_seguranca)+".")
    return redirect(url_for("ajuda.ajuda_index"))

@ajuda.route("/reclamacao_relato", methods=["POST","GET"])
def reclamacao_relato():
    if request.method == "POST":
        reclamacao = request.form["reclamacao"]
    elif request.method == "GET":
        reclamacao = request.args.get("reclamacao")
    global problema_reclamacao
    problema_reclamacao.append(str(reclamacao)+".")
    return redirect(url_for("ajuda.ajuda_index"))