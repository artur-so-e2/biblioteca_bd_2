import sqlite3 as sqlite

conn = sqlite.connect("biblioteca.bd")
conn.execute("DROP TABLE IF EXISTS usuarios")

sql_create = "CREATE TABLE usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100) NOT NULL)"
conn.execute(sql_create)

sql_insert = "INSERT INTO usuarios(nome) VALUES(?)"

conn.executemany(sql_insert, [('Eduardo',), ('Mariana',), ('Jôsevonio',)])
conn.commit()