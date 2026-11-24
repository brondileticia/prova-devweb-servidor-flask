"""
Factory da aplicação Flask.
Inicializa as extensões, registra o blueprint e os tratadores de erro.
"""
from datetime import datetime, timezone

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

from config import Config

# Extensões criadas sem app (factory pattern)
bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()


def create_app(config_class=Config):
    """Cria e configura a aplicação."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # Tratamento de erros
    # Os módulos sem rota (/professores, /alunos, /cursos, /ocorrencias) caem
    # aqui no 404 e exibem "Não disponível".
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html', current_time=datetime.now(timezone.utc)), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        db.session.rollback()
        return render_template('500.html', current_time=datetime.now(timezone.utc)), 500

    # Cria as tabelas na primeira execução (local e no PythonAnywhere)
    with app.app_context():
        from app import models  # noqa: F401
        db.create_all()

    return app
