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

# faça o upload do arquivo
```
