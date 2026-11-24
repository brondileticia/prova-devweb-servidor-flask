"""
Formulários (Flask-WTF).
"""
from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

from app import db
from app.models import Disciplina

SEMESTRES = [(str(n), f'{n}º semestre') for n in range(1, 7)]


class DisciplinaForm(FlaskForm):
    nome = StringField('Cadastre a nova disciplina e o semestre associado:',
                       validators=[DataRequired(message='Informe o nome da disciplina.'),
                                   Length(max=64)])
    semestre = RadioField('', choices=SEMESTRES,
                          validators=[DataRequired(message='Selecione o semestre.')])
    submit = SubmitField('Cadastrar')

    def validate_nome(self, field):
        """Impede cadastrar a mesma disciplina duas vezes (ignora maiúsculas/minúsculas).

        A comparação é feita em Python porque o lower() do SQLite não converte
        letras acentuadas (ex.: "MATEMÁTICA" x "matemática").
        """
        nome = field.data.strip().casefold()
        existentes = db.session.scalars(db.select(Disciplina.nome))
        if any(n.casefold() == nome for n in existentes):
            raise ValidationError('Disciplina já cadastrada.')
