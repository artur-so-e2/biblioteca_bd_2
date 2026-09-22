import sqlite3 as sqlite

conn = sqlite.connect("biblioteca.bd")
conn.execute("DROP TABLE IF EXISTS editoras")

sql_create = "CREATE TABLE editoras(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100) NOT NULL)"
conn.execute(sql_create)

sql_insert = "INSERT INTO editoras(nome) VALUES(?)"

conn.executemany(sql_insert, [('Falácia',), ('RáTodoPoderoso',)])
conn.commit()