# DB Python

Projeto desenvolvido durante meus estudos de Python e Banco de Dados, com foco na integração entre Python e SQLite.

O objetivo é praticar operações de banco de dados utilizando comandos SQL executados por meio da biblioteca `sqlite3` do Python.

## Tecnologias utilizadas

- Python
- SQLite3
- SQL

## Estrutura do projeto

| Arquivo | Descrição |
|---|---|
| `create_db.py` | Criação do banco de dados |
| `db.py` | Conexão com o banco e operações com estudantes e matrículas |
| `write_db.py` | Inserção de dados |
| `read_db.py` | Consulta e leitura de dados |
| `.gitignore` | Arquivos e pastas ignorados pelo Git |

## Funcionalidades e conceitos praticados

- Conexão com banco de dados SQLite.
- Criação de tabelas com `CREATE TABLE`.
- Inserção de registros com `INSERT INTO`.
- Consulta de dados com `SELECT`.
- Recuperação de registros com `fetchall()`.
- Utilização de cursores (`cursor`).
- Relacionamento entre tabelas.
- Persistência de dados com `commit()`.

## Como executar

1. Clone o repositório:

   `git clone https://github.com/annacm0/db_python.git`

2. Entre na pasta do projeto:

   `cd db_python`

3. Execute os arquivos Python conforme a operação que deseja testar:

   `python db.py`

**Observação:** o banco de dados SQLite pode ser criado localmente durante a execução dos scripts.

## Objetivo de aprendizagem

Consolidar os fundamentos de Python e SQL, desenvolvendo conhecimentos essenciais para programação Back-End e manipulação de bancos de dados relacionais.