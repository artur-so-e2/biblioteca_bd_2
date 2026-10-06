def inclui_livro(con, titulo, autor_id, editora_id, ano, edicao, disponivel):
    sql_insert = "INSERT INTO livros(titulo, autor_id, editora_id, ano_publicacao, edicao, disponivel) VALUES(?, ?, ?, ?, ?, ?)"
    con.execute(sql_insert, (titulo, autor_id, editora_id, ano, edicao, disponivel))
    con.commit()

def listar_livros(con):
    cursor = con.cursor()

    sql = "SELECT l.id, l.titulo, l.ano_publicacao, l.edicao, l.disponivel, a.nome as autor, e.nome as editora FROM livros l, autores a, editoras e WHERE (l.autor_id = autor.id) AND (l.editora_id = editora.id)"
    cursor.execute(sql)

    resultados = cursor.fetchall()

    for linha in resultados:
        print(f"ID: {linha['id']}    TÍTULO: {linha['titulo']}    ANO DE PUBLICAÇÃO: {linha['ano_publicacao']}    EDIÇÃO: {linha['edicao']}    DISPONIBILIDADE: {linha['disponivel']}    AUTOR: {linha['autor']}    EDITORA: {linha['editora']}")