# 📝 Avaliação Semestral — Flask + PythonAnywhere

Avaliação da disciplina **PTBDSWS — Desenvolvimento Web Servidor** (ADS · IFSP).
Rota implementada: **Cadastro de Disciplinas**.

🔗 **Aplicação no ar:** https://leticiabrondi.pythonanywhere.com/

<img width="1919" height="1030" alt="image" src="https://github.com/user-attachments/assets/a190a212-280d-4780-973b-8757e5c97523" />


---

## ✅ Recursos utilizados

| Recurso | Onde está |
|---|---|
| Hospedagem no PythonAnywhere | arquivo WSGI (ver abaixo) |
| Repositório no GitHub | este repositório |
| Construção de rotas | `app/main/routes.py` — somente `/` e `/disciplinas` |
| Tratamento de erros | `app/__init__.py` (`errorhandler` 404 e 500): os itens do menu sem rota exibem **"Não disponível"** |
| Templates e herança | `base.html` herda de `bootstrap/base.html`; as demais páginas herdam de `base.html` |
| Integração com Flask-Bootstrap | `Bootstrap()` em `app/__init__.py`; formulário com `wtf.form_field` (`bootstrap/wtf.html`) |
| Data e hora local | Flask-Moment: `moment(current_time).format('LLL')` na página inicial e na página "Não disponível" |
| Formulários | Flask-WTF — classe `DisciplinaForm` em `app/main/forms.py` |
| Persistência em banco de dados | Flask-SQLAlchemy — classe `Disciplina` em `app/models.py` (SQLite) |
| Recuperação e visualização | tabela "Relação de disciplinas cadastradas" em `/disciplinas` |

## 🗺️ Rotas

| Rota | Descrição |
|---|---|
| `/` | Nome, prontuário e data/hora local |
| `/disciplinas` | Formulário de cadastro + listagem do banco |
| `/professores`, `/alunos`, `/cursos`, `/ocorrencias` | **Rotas não criadas** — o tratamento de erro 404 mostra **"Não disponível"** |

## 📂 Estrutura

```
├── config.py              # Configurações (SECRET_KEY, banco, nome e prontuário)
├── run.py                 # Execução local
├── requirements.txt
├── print_tela_inicial.png # Print da tela inicial
└── app/
    ├── __init__.py        # Factory: extensões, blueprint, tratadores de erro, create_all
    ├── models.py          # class Disciplina
    ├── main/
    │   ├── __init__.py    # Blueprint
    │   ├── forms.py       # class DisciplinaForm (Flask-WTF)
    │   └── routes.py      # Rotas
    └── templates/
        ├── base.html  index.html  disciplinas.html
        └── 404.html ("Não disponível")  500.html
```

## 🚀 Executar localmente

```bash
python -m venv venv
source venv/bin/activate        # Windows: .\venv\Scripts\activate
pip install -r requirements.txt
python run.py                    # http://127.0.0.1:5000/
```

O banco `data.sqlite` é criado automaticamente na primeira execução.

## 🌐 Deploy no PythonAnywhere

1. **Consoles → Bash:**
   ```bash
   git clone https://github.com/brondileticia/prova-devweb-servidor-flask.git avaliacao
   cd avaliacao
   pip3.10 install --user -r requirements.txt
   ```
2. **Web → Add a new web app → Manual configuration → Python 3.10**.
3. **WSGI configuration file** — apague o conteúdo e use:
   ```python
   import sys
   import os

   path = '/home/leticiabrondi/avaliacao'
   if path not in sys.path:
       sys.path.append(path)

   os.environ['SECRET_KEY'] = 'troque-por-uma-chave-secreta'

   from app import create_app
   application = create_app()
   ```
4. **Reload**.

Para atualizar depois: `cd ~/avaliacao && git pull` e **Reload**.

---

**Letícia Brondi Carvalheiro** · Prontuário PT3037801 · ADS — IFSP
