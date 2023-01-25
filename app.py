import os
import dotenv
import psycopg2
from datetime import datetime
from flask import Flask, request
from flask_cors import cross_origin

dotenv.load_dotenv()

app = Flask(__name__)

@app.post('/upload')
@cross_origin()
def save_file():
    file = request.files.get("file")
    print("adasd",file)
    filename = file.filename

    if not os.path.isdir("uploads"):
        os.mkdir("uploads")

    file.save(os.path.join(f"uploads/{filename}"))

    with open(f"uploads/{filename}",'r') as f:
        transicoes = []

        for row in f:
            tipo = int(row[0:1])
            data = datetime.strptime(row[1:9],"%Y%m%d").strftime("%Y-%m-%d")
            valor = int(row[9:19])/100
            cpf = row[19:30]
            cartao = row[30:42]
            hora = row[42:48]
            dono_da_loja = row[48:62]
            nome_loja = row[62::]

            transicoes.append((tipo,data,valor,cpf,cartao,hora,dono_da_loja,nome_loja))

        with conn.cursor() as curs:
            curs.executemany("INSERT INTO transacao(tipo_id,data,valor,cpf,cartao,hora,dono_da_loja,nome_loja) VALUES (%s, %s, %s, %s, %s,%s, %s, %s)", transicoes)
            conn.commit()
      
    return {"message": "Sucesso!!"}

if __name__ == "__main__":

    conn = psycopg2.connect(database=os.getenv("POSTGRES_DB"),
                            host=os.getenv("HOST"),
                            user=os.getenv("POSTGRES_USER"),
                            password=os.getenv("POSTGRES_PASSWORD"),
                            port=os.getenv("PORT"))

    app.run(debug=True, port=5000, host="0.0.0.0")