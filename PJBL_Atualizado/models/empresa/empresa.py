from models import db

class Empresa(db.Model):
    __tablename__ = 'empresas'
    id = db.Column('id', db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    cnpj = db.Column(db.String(15), nullable=False, unique=True)
    description = db.Column(db.String(512))
