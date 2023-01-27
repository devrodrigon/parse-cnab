import os
from werkzeug.datastructures import FileStorage


def test_if_response_returns_status_200_sending_cnab_file(client):
    file = f"{os.getcwd()}/cnab.txt"

    my_file = FileStorage(
        stream=open(file, "rb"),
        filename="cnab.txt",
    )

    response = client.post("/upload", data={"file": my_file})

    assert response.status_code == 200
    assert response.json["message"] == "Sucesso!!"


def test_if_response_returns_status_400_sending_non_cnab_file(client):
    file = f"{os.getcwd()}/index.html"

    my_file = FileStorage(
        stream=open(file, "rb"),
        filename="index.html",
    )

    response = client.post("/upload", data={"file": my_file})

    assert response.status_code == 400
    assert response.json["message"] == "Ops, algo deu errado!!"
