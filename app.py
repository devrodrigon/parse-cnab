import os
from flask import Flask, request

app = Flask(__name__)

@app.post('/upload')
def save_file():
    file = request.files.get("file")
    filename = file.filename

    if not os.path.isdir("uploads"):
        os.mkdir("uploads")

    file.save(os.path.join(f"uploads/{filename}"))

    with open(f"uploads/{filename}",'r') as f:
        for row in f:
            print(row)
            
    return 'Bem vindo ao flask!'

if __name__ == "__main__":
    app.run(debug=True, port=5000)