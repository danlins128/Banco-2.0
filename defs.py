# Funções para o Banco 2.0
import os
import sqlite3
conn = sqlite3.connect('dados_cadastrais.db')

cursor = conn.cursor()

def limpar_console():
    sistema = os.name
    if sistema == 'posix': # Para linux
        os.system('clear')
    elif sistema == 'nt': # Para windows
        os.system('cls')
    else:
        pass

def criar_barra():
    print('-' * 32)

def carregar_dados():
    cursor.execute('SELECT * FROM dados_cadastrais')
    dados = cursor.fetchall()

def cadastrar_dados():
    while True:
        
        criar_barra()
        print(f'\033[1;33m'"--<<<Cadastrar novo usuário>>>-- "'\033[0;0m')
        criar_barra()
        
        nome = input("\nDigite seu nome: ")
        if nome != '0' and nome != '':
            login = input("Digite seu login: ")
            if login != '0' and login != '':
                senha = input("Digite sua senha: ")
                if senha != '0' and senha != '':
                    cursor.execute("SELECT * FROM usuarios WHERE login = ? AND senha = ?", (login, senha))
                    validar = cursor.fetchone()
                    if validar:
                        limpar_console()
                        criar_barra()
                        print('\033[1;31m'"--<<Usuário já cadastrado!>>--"'\033[0;0m')
                        print('\033[1;31m'"<Tente fazer login! 0 p/ voltar>"'\033[0;0m')
                        criar_barra()
        
                    else:
                        cursor.execute("INSERT INTO usuarios (nome, login, senha) VALUES (?, ?, ?)", (nome, login, senha))
                        conn.commit()            
                        limpar_console()
                        break
                    
                else:
                    break
            else:
                break
        else:
            break

        
        

def fazer_login():
    login = '.'
    while login == '.':
        print('-' * 42)
        print('\033[1;33m'"Digite seus dados abaixo para fazer login.\nDeixe em branco para retornar." '\033[0;0m')
        print('-' * 42)
        
        usuario_login = input("\nDigite seu login: ")

        if usuario_login != '':
            usuario_senha = input("Digite sua senha: ")
            if usuario_senha != '':
                cursor.execute("SELECT * FROM usuarios WHERE login = ? AND senha = ?", (usuario_login, usuario_senha))
                validar = cursor.fetchone()
                if validar:
                    limpar_console()
                    criar_barra()
                    print('\033[1;32m' "Login efetuado com sucesso!" '\033[0;0m')
                    criar_barra()                    
                    acessar_sistema()
                    login = ','                            
                else:
                    limpar_console()
                    print('-' * 42)
                    print('\033[1;31m' "Usuário ou senha incorretos!"'\033[0;0m' )
            else:
                break
        else:
            break
    

def acessar_sistema():
    while True:
        
        criar_barra()
        print(f'\033[1;34m' "Seja bem vindo ao Daniel's Bank" '\033[0;0m')
        print(f'\033[1;34m' "O que deseja fazer hoje?" '\033[0;0m')
        criar_barra()
        print(f'\033[1;36m' "[1]" '\033[0;0m' " Depositar")
        print(f'\033[1;36m' "[2]" '\033[0;0m' " Sacar")
        print(f'\033[1;36m' "[3]" '\033[0;0m' " Transferir")
        print(f'\033[1;36m' "[4]" '\033[0;0m' " Configuração")
        print(f'\033[1;36m' "[5]" '\033[0;0m' " Desconectar")

        escolha = input('\n:')

        if escolha == '1':
            depositar()
        if escolha == '2':
            sacar()
        #if escolha == '3':
            
        #if escolha == '4':

        if escolha == '5':
            break
        else:
            print('Opção inválida.')

    
def depositar():
    d = 'ficar'
    limpar_console()
    while d == 'ficar':
        criar_barra()
        print('\033[1;33m' '--------<< Depositar >>---------' '\033[0;0m')
        criar_barra()
        
        print('Deixe em branco para voltar!')
        criar_barra()
        valor_a_depositar = input('Informe o valor que você quer depositar: ')
        
        if valor_a_depositar == '':
            d = 'sair'
            limpar_console()

        elif not valor_a_depositar.isdigit() or int(valor_a_depositar) == 0:
            limpar_console()
            print('\nValor inexistente! Digite um valor válido\n')
            
        
        else:
            valor_a_depositar = float(valor_a_depositar)            
            cursor.execute('UPDATE usuarios SET saldo = saldo + ?', (valor_a_depositar,))
            conn.commit()
            print(f"\nDeposito de R${valor_a_depositar} efetuado com sucesso.")
            criar_barra()
            
            print(f'\033[1;36m' "[S]" '\033[0;0m' " Depositar novamente")
            print(f'\033[1;36m' "[N]" '\033[0;0m' " Voltar")
            opçao = input('\n')
            if opçao.lower() == 'n':
                d = 'sair'
                limpar_console()
            elif opçao.lower() == 's':
                limpar_console()                
            else:
                limpar_console()
                print('\nOpção inválida')
                break
                    
def sacar():
    d = 'ficar'
    limpar_console()
    while d == 'ficar':
        criar_barra()
        print('\033[1;33m' '--------<< Sacar >>---------' '\033[0;0m')
        criar_barra()

        print('Deixe em branco para voltar!')
        criar_barra()
        valor_a_sacar = input('Informe o valor que você quer sacar: ')

        if valor_a_sacar == '':
            d = 'sair'
            limpar_console()

        elif valor_a_sacar.isalpha() and float(valor_a_sacar) == '0':
            limpar_console()
            print('\nValor inexistente! Digite um valor válido\n')
        else:
            valor_a_sacar = float(valor_a_sacar)
            cursor.execute('UPDATE usuarios SET saldo = saldo - ?', (valor_a_sacar))
            conn.commit()
            print(f'Saque de R${valor_a_sacar} efetuado com sucesso')
            criar_barra()

            print(f'\033[1;36m' "[S]" '\033[0;0m' " Sacar novamente")
            print(f'\033[1;36m' "[N]" '\033[0;0m' " Voltar")
            opçao = input('\n')
            if opçao.lower() == 'n':
                d = 'sair'
                limpar_console()
            elif opçao.lower() == 's':
                limpar_console()                
            else:
                limpar_console()
                print('\nOpção inválida')
                break