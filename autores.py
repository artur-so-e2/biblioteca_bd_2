import sqlite3 as sqlite

conn = sqlite.connect("biblioteca.bd")
conn.execute("DROP TABLE IF EXISTS autores")

sql_create = "CREATE TABLE autores(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100) NOT NULL)"
conn.execute(sql_create)

sql_insert = "INSERT INTO autores(nome) VALUES(?)"

conn.executemany(sql_insert, [('José',), ('Pitágoras',), ('Isaac B.',), ('Letucia',)])
conn.commit()