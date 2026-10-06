def inclui_autor(con, nome):
    con.execute("INSERT INTO autores(nome) VALUES(?)", (nome,))
    con.commit()

def get_id_autor(con, nome_autor):
    cursor = con.cursor()

    cursor.execute(f"SELECT id FROM autores WHERE nome = '{nome_autor}'")
    resultado = cursor.fetchone()
    return resultado[0]


def lista_autores(con):
    cursor = con.cursor()

    cursor.execute("SELECT * FROM autores")

    resultados = cursor.fetchall()

    for linha in resultados:
        print(f"ID: {linha['id']}    NOME: {linha['nome']}")