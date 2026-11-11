import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# cursor.execute(
#     """SELECT * FROM estudantes""" #consultar bd
# )

cursor.execute(
    """SELECT * FROM disciplinas""" #consultar bd
)

conn.commit()

disciplinas = cursor.fetchall() #pegar todas as disciplinas
for disciplina in disciplinas:
    print(disciplina)

# estudantes = cursor.fetchall() #pegar todos os estudantes
# for estudante in estudantes:
#     print(estudante)