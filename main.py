import sqlite3 as sqlite
from util import limpa_tela
from usuarios import inclui_usuario, lista_usuario

conn = sqlite.connect("biblioteca.bd")
conn.row_factory = sqlite.Row

def menu_usuarios():
    while(True):
        limpa_tela()
        print("-"*10, "Menu Usuários", "-"*10, "\n1 - Adicionar\n2 - Listar")
        opcao = input("Digite a opção que deseja fazer em usuários: ")

        if opcao == '1':
            nome_usuario = input("Digite o nome do novo usuário: ")
            inclui_usuario(conn, nome_usuario)
        elif opcao == '2':
            lista_usuario(conn)
            input("Aperte 'Enter' para continuar.")
        elif opcao == '3':
            limpa_tela()
            break
        else:
            input("Erro, tente novamete. Aperte 'Enter' para continuar.")

while(True):
    print("="*15, "MENU PRINCIPAL", "="*15)
    print("1 - Usuários")
    print("2 - Autores")
    print("3 - Editoras")
    print("4 - Livros")
    print("5 - Empréstimos")

    escolha = input("Digite a opção que deseja realizar: ")

    if escolha == '1':
        menu_usuarios()