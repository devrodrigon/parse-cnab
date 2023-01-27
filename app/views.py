import os
import dotenv
import psycopg2
from flask import Blueprint, request, make_response, abort
from datetime import datetime
from flask_cors import cross_origin
from .models import Tipo, Transacao
from .app import db

dotenv.load_dotenv()

api = Blueprint("api", __name__)


@api.post("/upload")
@cross_origin()
def save_file():
    try:
        file = request.files.get("file")
        filename = file.filename

        if not os.path.isdir("uploads"):
            os.mkdir("uploads")

        file.save(os.path.join(f"uploads/{filename}"))

        with open(f"uploads/{filename}", "r") as f:
            for row in f:
                tipo = int(row[0:1])
                data = datetime.strptime(row[1:9], "%Y%m%d").strftime("%Y-%m-%d")
                data_python = datetime.strptime(row[1:9], "%Y%m%d").date()
                valor = int(row[9:19]) / 100
                cpf = row[19:30]
                cartao = row[30:42]
                hora = row[42:48]
                hora_python = datetime.strptime(row[42:48], "%H%M%S").time()
                dono_da_loja = row[48:62]
                nome_loja = row[62::]

                tipo_obj = Tipo.query.filter_by(id=tipo).first()
                transacao = Transacao(
                    tipo=tipo_obj,
                    nome_loja=nome_loja,
                    dono_da_loja=dono_da_loja,
                    cpf=cpf,
                    cartao=cartao,
                    valor=valor,
                    hora=hora_python,
                    data=data_python,
                )
                db.session.add(transacao)
                db.session.commit()

        return make_response({"message": "Sucesso!!"}, 200)

    except Exception:
        abort(make_response({"message": "Ops, algo deu errado!!"}, 400))
