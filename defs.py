# Funções para o Banco 2.0
import sqlite3
conn = sqlite3.connect('dados_cadastrais.db')

cursor = conn.cursor()

def carregar_dados():
    cursor.execute('SELECT * FROM dados_cadastrais')
    dados = cursor.fetchall()

def cadastrar_dados():
    while True:
        print(f"Cadastrar novo usuário:\n")
        nome = input("Digite seu nome: ")
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")
        cursor.execute("SELECT * FROM usuarios WHERE login = ? AND senha = ?", (login, senha))
        validar = cursor.fetchone()
        if validar:
            print("\nUsuário já cadastrado, escolha outro 'Login'\n")
        else:
            cursor.execute("INSERT INTO usuarios (nome, login, senha) VALUES (?, ?, ?)", (nome, login, senha))
            conn.commit()
            break

def acessar_sistema():
    usuario_login = input("\nDigite seu login: ")
    usuario_senha = input("Digite sua senha: ")
    cursor.execute("SELECT * FROM usuarios WHERE login = ? AND senha = ?", (usuario_login, usuario_senha))
    validar = cursor.fetchone()
    
    if validar:
        print("\nLogin efetuado com sucesso!\n")
    else:
        print("\nUsuário ou senha incorretos!\n")