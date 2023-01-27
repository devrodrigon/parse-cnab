from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///parse-cnab.sqlite3"
    db.init_app(app)

    from .models import Tipo, Transacao

    @app.cli.command("create_tables")
    def create_tables():
        with app.app_context():
            db.create_all()
            debito = Tipo(descricao="Débito", natureza="Entrada", sinal="+")
            db.session.add(debito)
            boleto = Tipo(descricao="Boleto", natureza="Saída", sinal="-")
            db.session.add(boleto)
            financiamento = Tipo(descricao="Financiamento", natureza="Saída", sinal="-")
            db.session.add(financiamento)
            credito = Tipo(descricao="Credito", natureza="Entrada", sinal="+")
            db.session.add(credito)
            emprestimo = Tipo(descricao="Recebimento de Empréstimo", natureza="Entrada", sinal="+")
            db.session.add(emprestimo)
            vendas = Tipo(descricao="Vendas", natureza="Entrada", sinal="+")
            db.session.add(vendas)
            ted = Tipo(descricao="Recebimento TED", natureza="Entrada", sinal="+")
            db.session.add(ted)
            doc = Tipo(descricao="Recebimento DOC", natureza="Entrada", sinal="+")
            db.session.add(doc)
            aluguel = Tipo(descricao="Aluguel", natureza="Saída", sinal="-")
            db.session.add(aluguel)
            db.session.commit()

    from .views import api
    app.register_blueprint(api)

    return app