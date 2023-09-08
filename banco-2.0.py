import defs
import sqlite3
conn = sqlite3.connect('dados_cadastrais.db')

cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios(
            nome TEXT,
            login TEXT,
            senha TEXT,
            saldo REAL               
)
''')

'''
 Código para inserir novos dados.

cursor.execute("INSERT INTO usuarios (nome, login, senha) VALUES (?, ?, ?)", (nome, login, senha))

 Código para validar dados.

cursor.execute("SELECT * FROM tabela_de_usuarios WHERE login = ? AND senha = ?", (usuario_login, usuario_senha))
resultado = cursor.fetchone()

 Código para adicionar coluna na tabela

cursor.execute('ALTER TABLE usuarios ADD COLUMN saldo NUMERIC')
'''

if __name__ == '__main__':
    while True:
        print(f"Seja bem vindo ao Daniel's Bank\n")
        print(f"[1.] Criar Conta")
        print(f"[2.] Fazer Login")
        print(f"[3.] Sair")
        escolha = input()

        if escolha == "1":
            defs.cadastrar_dados()
        elif escolha == "2":
            defs.validar_dados()
        elif escolha == "3":
            print("Obrigado por usar nosso sistema!")
            conn.close()
            break
        else:
            print("Escolha inválida, tente outra.\n")