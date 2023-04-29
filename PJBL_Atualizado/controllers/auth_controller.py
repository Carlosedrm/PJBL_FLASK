from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, login_required, logout_user
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash
from models.auth.user import User
from models.db import db

auth = Blueprint("auth", __name__, template_folder="./views/", static_folder='./static/', root_path="./")

logins = []
saved_funcionario = []

@auth.route("/")
@auth.route("/login")
def login():
    return render_template("auth/Login.html")

@auth.route("/cadastrar")
def cadastrar():
    return render_template("auth/Cadastro.html")

# Coisas para cadastro

@auth.route("/listaFuncionario")
def funcionario_index():
    global saved_funcionario
    return render_template("listagem/ListaFuncionario.html", funcionarios = saved_funcionario)

@auth.route("/save_funcionario", methods=["POST","GET"])
def save_funcionario():
    if request.method == "POST":
        nome_funcionario = request.form["nome_funcionario"]
        usuario_funcionario = request.form["usuario_funcionario"]
        email_funcionario = request.form["email_funcionario"]
        contato_funcionario = request.form["contato_funcionario"]
        cpf_funcionario = request.form["cpf_funcionario"]
        sexo_funcionario = request.form["sexo_funcionario"]
        idade_funcionario = request.form["idade_funcionario"]
        senha_funcionario = request.form["senha_funcionario"]

    global saved_funcionario
    saved_funcionario.append(str(nome_funcionario)+", " +str(usuario_funcionario)+ ", "+str(email_funcionario)+", "+str(contato_funcionario)+", " +str(cpf_funcionario)+", " +str(sexo_funcionario)+", " +str(idade_funcionario)+", " +str(senha_funcionario))
    
    # Coisas para a autenticação
    user = User.query.filter_by(email=email_funcionario).first()

    if user:
        # Mostrar o Flask
        flash('Esse E-mail ou Usuario já existe!')
        return redirect(url_for('auth.cadastrar'))
    
    new_user = User(name=nome_funcionario, username=usuario_funcionario, email=email_funcionario, contato=contato_funcionario, sexo=sexo_funcionario,idade=idade_funcionario,password=senha_funcionario)
    #new_user = User(email=email, name=name, username=username, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("auth.funcionario_index"))


# Coisas para login

@auth.route("/loginaceito")
def loginaceito():
    return redirect(url_for("auth.funcionario_index"))

@auth.route("/login_salvo", methods=["POST"])
def login_salvo():
    usuario = request.form.get("usuario")
    senha = request.form.get("password")

    user = User.query.filter((User.username==usuario) | (User.email==usuario)).first()

    if not user or not senha==senha:
        flash('Usuário ou Senha incorretos!')
        return redirect(url_for('auth.login'))
    
    global logins
    logins.append("Usuario: " + str(usuario) + "Senha: " + str(senha))

    return redirect(url_for("auth.loginaceito"))

# Coisas para a autenticação

