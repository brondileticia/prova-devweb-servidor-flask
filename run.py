"""
Ponto de entrada para execução LOCAL: python run.py
No PythonAnywhere quem chama create_app() é o arquivo WSGI.
"""
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
