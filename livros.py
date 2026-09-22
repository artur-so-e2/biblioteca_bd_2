import sqlite3 as sqlite

conn = sqlite.connect("biblioteca.bd")
conn.execute("DROP TABLE IF EXISTS usuarios")

sql_create = "CREATE TABLE livros(id INTEGER PRIMARY KEY AUTOINCREMENT, titulo VARCHAR(140) NOT NULL, autor_id INTEGER REFERENCES autores(id), editora_id INTEGER REFERENCES editoras(id), ano_publicacao INTEGER, edicao INTEGER, disponivel BOOLEAN NOT NULL DEFAULT 1 CHECK (disponivel IN(0,1)))"
conn.execute(sql_create)

sql_insert = "INSERT INTO livros(titulo, autor_id, editora_id, ano_publicacao, edicao, disponivel) VALUES(?, ?, ?, ?, ?, ?)"

conn.executemany(sql_insert, [('Livro do José', 1, 1, 2001, 1, 1), ('A alface mais verde', 4, 1, 2014, 2,0), ('Entendendo triângulos', 2, 2, '522 a.C', 1, 1), ('Caiu uma bíblia na minha mãe, o que faço agora? "Edição Polyphemus"', 3, 2, 2011, 4, 0)])
conn.commit()