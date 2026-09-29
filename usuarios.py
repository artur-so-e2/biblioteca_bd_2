def inclui_usuario(conn, nome_usuario):
    conn.execute("INSERT INTO usuarios(nome VALUES(?)", (nome_usuario,))
    conn.commit()

def lista_usuario(conn):
    cursor = conn.cursor()

    resultados = cursor.fetchall()

    for linha in resultados:
        print(f"ID: {linha['id']}    NOME: {linha['nome']}")