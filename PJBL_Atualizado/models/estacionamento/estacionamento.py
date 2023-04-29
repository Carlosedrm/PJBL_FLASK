from models import db

class Estacionamento(db.Model):
    __tablename__ = 'estacionamentos'
    id = db.Column('id', db.Integer(), primary_key=True)
    description = db.Column(db.String(512))