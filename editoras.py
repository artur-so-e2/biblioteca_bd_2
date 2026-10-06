def inclui_editora(con, nome):
    con.execute("INSERT INTO editoras(nome) VALUES(?)", (nome,))
    con.commit()

def get_id_editora(con, nome_editora):
    cursor = con.cursor()

    cursor.execute(f"SELECT id FROM editoras WHERE nome = '{nome_editora}'")
    resultado = cursor.fetchone()
    return resultado[0]


def lista_editoras(con):
    cursor = con.cursor()

    cursor.execute("SELECT * FROM editoras")

    resultados = cursor.fetchall()

    for linha in resultados:
        print(f"ID: {linha['id']}    NOME: {linha['nome']}")