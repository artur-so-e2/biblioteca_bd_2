import sqlite3 as sqlite
from util import limpa_tela

from usuarios import inclui_usuario, lista_usuarios
from autores import inclui_autor, lista_autores, get_id_autor
from editoras import inclui_editora, lista_editoras, get_id_editora
#from emprestimos import inclui_emprestimo, lista_emprestimos

conn = sqlite.connect("biblioteca.db")
conn.row_factory = sqlite.Row

def menu_usuarios():
    while (True):
        limpa_tela()
        print("-"*10, "Menu de usuários", "-"*10)
        print("1 - Incluir novo usuário\n2 - Listar usuários\n3 - Voltar para o menu principal")
        opcao = input("Digite a opção que deseja fazer em usuários: ")
        if (opcao == '1'):
            nome = input("Digite o nome do novo usuário: ")
            inclui_usuario(conn, nome)
        elif (opcao == '2'):
            lista_usuarios(conn)
            input("Aperte 'Enter' para continuar...")
        elif (opcao == '3'):
            limpa_tela()
            break
        else:
            input("Opção inválida! Aperte 'Enter' para continuar...")

def menu_autores():
    while (True):
        limpa_tela()
        print("-"*10, "Menu de autores", "-"*10)
        print("1 - Incluir novo autor\n2 - Listar autores\n3 - Voltar para o menu principal")
        opcao = input("Digite a opção que deseja fazer em autores: ")
        if (opcao == '1'):
            nome = input("Digite o nome do novo autor: ")
            inclui_autor(conn, nome)
        elif (opcao == '2'):
            lista_autores(conn)
            input("Aperte 'Enter' para continuar...")
        elif (opcao == '3'):
            limpa_tela()
            break
        else:
            input("Opção inválida! Aperte 'Enter' para continuar...")

def menu_editoras():
    while (True):
        limpa_tela()
        print("-"*10, "Menu de editoras", "-"*10)
        print("1 - Incluir nova editora\n2 - Listar editoras\n3 - Voltar para o menu principal")
        opcao = input("Digite a opção que deseja fazer em editoras: ")
        if (opcao == '1'):
            nome = input("Digite o nome do nova editora: ")
            inclui_editora(conn, nome)
        elif (opcao == '2'):
            lista_editoras(conn)
            input("Aperte 'Enter' para continuar...")
        elif (opcao == '3'):
            limpa_tela()
            break
        else:
            input("Opção inválida! Aperte 'Enter' para continuar...")

def menu_livros():
    while (True):
        limpa_tela()
        print("-"*10, "Menu de livros", "-"*10)
        print("1 - Incluir novo livro\n2 - Listar livros\n3 - Voltar ao menu principal")
        opcao = input("Digite a opção que deseja fazer em livros: ")
        if (opcao == '1'):
            titulo = input("Digite o título do novo livro: ")
            nome_autor = input("Digite o nome do autor: ")
            id_autor = get_id_autor(conn, nome_autor)
            nome_editora = input("Digite o nome da editora: ")
            id_editora = get_id_editora(conn, nome_editora)
            ano_publicacao = int(input("Digite o ano de publicação: "))
            edicao = int(input("Digite a edição: "))
            disponivel_text = input("Digite se o livro está disponivel (S/N): ").upper
            if disponivel_text == 'S':
                disponivel = True
            elif disponivel_text == 'N':
                disponivel == False
            else:
                input("Opção inválida! Aperte 'Enter' para continuar...")
                break
            inclui_editora(conn, titulo, id_autor, id_editora, ano_publicacao, edicao, disponivel)
        elif (opcao == '2'):
            lista_editoras(conn)
            input("Opção inválida! Aperte 'Enter' para continuar...")
        elif (opcao == '3'):
            limpa_tela()
            break
        else:
            input("Opção inválida! Aperte 'Enter' para continuar...")

def menu_emprestimos():
    while (True):
        limpa_tela()
        print("-"*10, "Menu de Empréstimos", "-"*10)
        print("(1)-Incluir novo impréstimo\n(2)-Listar\n(3)-Voltar")
        opcao = input("Digite a opção: ")
        if (opcao == '1'):
            usuario = 1
            livros = []
            while (True):
                titulo_livro = input("Digite o título do livro: ")
                livros.append(titulo_livro)
                opcao = input("Digite S para incluir novo livro ou qualquer tecla para fechar a lista.")
                if (opcao.upper() != 'S'):
                    break
            inclui_emprestimo(conn, usuario, livros)
        elif (opcao == '2'):
            lista_emprestimos(conn)
            input("Digite uma tecla para continuar...")
        elif (opcao == '3'):
            limpa_tela()
            break
        else:
            input("Opção inválida! Digite uma tecla para continuar...")


while (True):
    limpa_tela()
    print("===== Sistema da biblioteca ======")
    print("(1)-Usuários\n(2)-Autores\n(3)-Editoras\n(4)-Livros")
    opcao = input("Digite a opção: ")

    if (opcao == '1'):
        menu_usuarios()
    elif (opcao == '2'):
        menu_autores()
    elif (opcao == '3'):
        menu_editoras()
    elif (opcao == '4'):
        menu_livros()
    elif (opcao == '5'):
        menu_emprestimos()
    else:
        break

#fecha a conexão
conn.close()