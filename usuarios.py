def inclui_usuario(con, nome):
    con.execute("INSERT INTO usuarios(nome) VALUES(?)", (nome,))
    con.commit()

def lista_usuarios(con):
    cursor = con.cursor()

    cursor.execute("SELECT * FROM usuarios")

    resultados = cursor.fetchall()

    for linha in resultados:
        print(f"ID: {linha['id']}    NOME: {linha['nome']}")