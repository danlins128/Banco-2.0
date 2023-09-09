import defs
import sqlite3
conn = sqlite3.connect('dados_cadastrais.db')

cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                login TEXT UNIQUE NOT NULL,
                senha TEXT NOT NULL,
                saldo REAL DEFAULT 0.0 NOT NULL             
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
        defs.limpar_console()
        defs.criar_barra()
        print(f'\033[1;34m' "Seja bem vindo ao Daniel's Bank" '\033[0;0m')
        defs.criar_barra()
        print(f'\033[1;36m' "[1]" '\033[0;0m' " Criar Conta")
        print(f'\033[1;36m' "[2]" '\033[0;0m' " Fazer Login")
        print(f'\033[1;36m' "[3]" '\033[0;0m' " Sair...")
        
        escolha = input('\n')

        if escolha == "1":
            defs.limpar_console()
            defs.cadastrar_dados()
        elif escolha == "2":
            defs.limpar_console()
            defs.fazer_login()
        elif escolha == "3":
            defs.limpar_console()
            print('\033[1;31m'"Obrigado por usar nosso sistema!" '\033[0;0m')
            conn.close()
            break
        else:
            print("Escolha inválida, tente outra.\n")