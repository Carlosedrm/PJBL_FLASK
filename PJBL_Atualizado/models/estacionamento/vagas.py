from models import db, Estacionamento

class Vaga(db.Model):
    __tablename__ = 'vagas'
    id = db.Column('id', db.Integer(), primary_key=True)
    andar = db.Column(db.Integer(), nullable=False)
    id_estacionamento = db.Column(db.Integer(), db.ForeignKey(Estacionamento.id, ondelete='CASCADE'))