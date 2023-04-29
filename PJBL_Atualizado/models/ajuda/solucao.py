from models import db
from datetime import datetime

class Solucao(db.Model):
    __tablename__ = 'solucoes'
    id = db.Column('id', db.Integer(), primary_key=True)
    data_hora = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    description = db.Column(db.String(512))