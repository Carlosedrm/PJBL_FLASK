from models import db

class Chamada(db.Model):
    __tablename__ = 'chamadas'
    id = db.Column('id', db.Integer(), primary_key=True)
    description = db.Column(db.String(512))