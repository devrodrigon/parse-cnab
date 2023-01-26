# PARSE-CNAB

## DESAFIO BACKEND

## SOBRE O DESAFIO

Você recebeu um arquivo CNAB com os dados das movimentações financeiras de várias lojas. Precisamos
criar uma maneira para que estes dados sejam importados para um banco de dados.

Sua tarefa é criar uma interface web que aceite upload do arquivo CNAB, normalize os dados e
armazene-os em um banco de dados relacional e exiba essas informações em tela.

## TECNOLOGIAS USADAS

- Python
- Flask
- HTLM
- JavaScript
- docker

## EXECUTAR PROJETO USANDO DOCKER

```bash
# Fazer o clone do projeto
git clone git@github.com:devrodrigon/parse-cnab.git

# Acesse a pasta do projeto
cd parse-cnab

# Executar os containers
docker compose up

# O servidor da api iniciará na porta: 5000

# O servidor web iniciará na porta: 8080 - acesse <http://localhost:8080>

# faça o upload do arquivo cnab.txt
```

## Executar projeto sem docker

```bash
# Fazer o clone do projeto
git clone git@github.com:devrodrigon/parse-cnab.git

# Acesse a pasta do projeto
cd parse-cnab

# Criar um ambiente virtual
python -m venv venv

# Ative seu venv
# No linux
source venv/bin/activate

# No windows
.\venv\Scripts\activate

# Rode as dependencias
pip install -r requirements.txt

# Crie um banco de dados postgres pelo terminal
psql -U <seu_nome_de_usuario> -c "create database cnab;"

# Crie as tabelas usando o arquivo db.sql
psql -U <seu_nome_de_usuario> -d cnab -f db.sql

# Faça uma copia do arquivo .env.example e renomei para .env
cat .env.example > .env

# Informe os dados no arquivo .env

# Execute a aplicação
python app/app.py

# O servidor iniciará na porta: 5000

# Abra o arquivo index.html em um navegador e faça o upload do arquivo cnab.txt
```

## Rodar os testes

```bash
# Execute os passos de cima(não precisa executar a aplicação)

# Rode os tests
pytest -v
```
