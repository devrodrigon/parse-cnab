CREATE DATABASE IF NOT EXISTS cnab;

\c cnab

CREATE TABLE IF NOT EXISTS tipo (
    tipo BIGSERIAL PRIMARY KEY,
    descricao VARCHAR(50) UNIQUE,
    natureza VARCHAR(50) NOT NULL,
    sinal VARCHAR(1) NOT NULL
);

INSERT INTO tipo
    (tipo, descricao, natureza, sinal)
VALUES
    (1, 'Débito', 'Entrada', '+'),
    (2, 'Boleto', 'Saída', '-'),
    (3, 'Financiamento', 'Saída', '-'),
    (4, 'Crédito', 'Entrada', '+'),
    (5, 'Recebimento Empréstimo', 'Entrada', '+'),
    (6, 'Vendas', 'Entrada', '+'),
    (7, 'Recebimento TED', 'Entrada', '+'),
    (8, 'Recebimento DOC', 'Entrada', '+'),
    (9, 'Aluguel', 'Saída', '-');


CREATE TABLE IF NOT EXISTS transacao(
    id BIGSERIAL PRIMARY KEY,
    nome_loja VARCHAR(255) NOT NULL,
    dono_da_loja VARCHAR(255) NOT NULL,
    cpf VARCHAR(11) NOT NULL,
    cartao VARCHAR(12) NOT NULL,
    valor VARCHAR(10) NOT NULL,
    data DATE NOT NULL,
    hora TIME NOT NULL,
    tipo_id INTEGER,
    FOREIGN KEY (tipo_id) REFERENCES tipo(tipo) ON DELETE CASCADE  
);
