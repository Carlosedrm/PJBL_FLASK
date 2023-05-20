from models import *
from werkzeug.security import generate_password_hash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

def generate_seeds(db:SQLAlchemy):
    # Algumas vagas
    v1 = Vaga(andar = 1)
    v2 = Vaga(andar = 2)
    v3 = Vaga(andar = 2)

    db.session.add_all([v1, v2, v3])
    db.session.commit()

    # Algumas chamadas de concerto
    c1 = Conserto(numero_vaga = v1.id, descricao  = "Sensor não detecta presença", status = "Inconcluido")
    c2 = Conserto(numero_vaga = v1.id, descricao  = "Sensor está quebrado", status = "Inconcluido")
    c3 = Conserto(numero_vaga = v3.id, descricao  = "Sensor não recebe energia", status = "Inconcluido")

    db.session.add_all([c1, c2, c3])
    db.session.commit()

    # As roles que um úsuario pode ter

    role1 = Role(nome = "Admin", descricao = "Admin capaz de acessar a maioria das páginas")
    role2 = Role(nome = "Funcionario", descricao = "Funcionario capaz de acessar certas páginas")

    db.session.add_all([role1,role2])
    db.session.commit()

    # Alguns usuarios
    u1 = User(name = "Roberto Junior", username = "Roberto", cpf = "11567812689", email = "Roberto@gmail.com", contato = "41 997287165", sexo = "Masculino", idade = "35", password = "Senha")
    u1.roles = [role1]

    db.session.add_all([u1])
    db.session.commit()

    # A empresa
    empresa = Empresa(nome = "ANATEL", cnpj = "1234567891011", descricao = "A empresa responsavel por tudo")

    db.session.add_all([empresa])
    db.session.commit()

    # O estacionamento

    estacionamento = Estacionamento()
    db.session.add_all([estacionamento])
    db.session.commit()

