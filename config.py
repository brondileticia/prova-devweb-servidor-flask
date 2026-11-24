"""
Configurações centralizadas da aplicação.
"""
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Configurações base."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'chave-secreta-avaliacao-ptbdsws')

    # Caminho absoluto: no PythonAnywhere o diretório de trabalho não é a pasta do projeto
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Dados exibidos na rota principal
    ALUNO_NOME = 'Letícia Brondi Carvalheiro'
    ALUNO_PRONTUARIO = 'PT3037801'
