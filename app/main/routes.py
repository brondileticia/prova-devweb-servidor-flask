"""
Rotas da aplicação.

Somente a rota principal (/) e o Cadastro de Disciplinas (/disciplinas) existem.
Os demais itens do menu (/professores, /alunos, /cursos, /ocorrencias) NÃO têm
rota: o acesso cai no tratamento de erro 404, que mostra "Não disponível"
(ver app/__init__.py).
"""
from datetime import datetime, timezone

from flask import current_app, redirect, render_template, url_for
from sqlalchemy.exc import IntegrityError

from app import db
from app.main import bp
from app.main.forms import DisciplinaForm
from app.models import Disciplina


@bp.route('/')
def index():
    return render_template('index.html',
                           nome=current_app.config['ALUNO_NOME'],
                           prontuario=current_app.config['ALUNO_PRONTUARIO'],
                           current_time=datetime.now(timezone.utc))


@bp.route('/disciplinas', methods=['GET', 'POST'])
def disciplinas():
    form = DisciplinaForm()
    if form.validate_on_submit():
        disciplina = Disciplina(nome=form.nome.data.strip(),
                                semestre=int(form.semestre.data))
        db.session.add(disciplina)
        try:
            db.session.commit()
            return redirect(url_for('main.disciplinas'))  # Post/Redirect/Get
        except IntegrityError:
            db.session.rollback()
            form.nome.errors.append('Disciplina já cadastrada.')

    lista = Disciplina.query.order_by(Disciplina.id).all()
    return render_template('disciplinas.html', form=form, disciplinas=lista)
