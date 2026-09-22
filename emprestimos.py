import sqlite3 as sqlite

conn = sqlite.connect("biblioteca.bd")
conn.execute("DROP TABLE IF EXISTS emprestimos")

sql_create = "CREATE TABLE emprestimos(id INTEGER PRIMARY KEY AUTOINCREMENT, usuario_id INTEGER REFERENCES usuarios(id), data DATE DEFAULT CURRENT_DATE)"
conn.execute(sql_create)

sql_insert = "INSERT INTO emprestimos(usuario_id) VALUES(?)"

conn.executemany(sql_insert, [(2,), (1,)])
conn.commit()