"""
Modelos do banco de dados.
"""
from app import db


class Disciplina(db.Model):
    __tablename__ = 'disciplinas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), unique=True, nullable=False, index=True)
    semestre = db.Column(db.Integer, nullable=False)

    @property
    def semestre_descricao(self):
        return f'{self.semestre}º semestre'

    def __repr__(self):
        return f'<Disciplina {self.nome} ({self.semestre_descricao})>'
