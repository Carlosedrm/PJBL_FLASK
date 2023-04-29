from models import db

class Vaga(db.Model):
    __tablename__ = 'vagas'
    id = db.Column('id', db.Integer(), primary_key=True)
    andar = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(512))