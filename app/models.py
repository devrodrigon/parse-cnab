from .app import db


class Tipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(50), unique=True, nullable=False)
    natureza = db.Column(db.String(50), nullable=False)
    sinal = db.Column(db.String(1), nullable=False)
    transacoes = db.relationship("Transacao", backref="tipo")


class Transacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_loja = db.Column(db.String(255), nullable=False)
    dono_da_loja = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    cartao = db.Column(db.String(12), nullable=False)
    valor = db.Column(db.String(10), nullable=False)
    data = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    tipo_id = db.Column(db.Integer, db.ForeignKey("tipo.id"))
