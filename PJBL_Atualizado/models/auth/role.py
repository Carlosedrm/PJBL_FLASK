from models import db
from models import db, User

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column('id', db.Integer(), primary_key=True)
    funcionario = db.Column("id_user", db.Integer(), db.ForeignKey(User.id))
    name = db.Column(db.String(50))
    description = db.Column(db.String(512))

    users = db.Relationship("User", back_populates="roles", secondary="user_roles")