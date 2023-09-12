# Funções para o Banco 2.0
import time
import os
import sqlite3
conn = sqlite3.connect('dados_cadastrais.db')

cursor = conn.cursor()

usuario_login = None

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
    global usuario_login
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
        limpar_console()
        criar_barra()
        print(f'\033[1;34m' "Seja bem vindo ao Daniel's Bank" '\033[0;0m')
        print(f'\033[1;34m' "O que deseja fazer hoje?" '\033[0;0m')
        criar_barra()
        print(f'\033[1;36m' "[1]" '\033[0;0m' " Depositar")
        print(f'\033[1;36m' "[2]" '\033[0;0m' " Sacar")
        print(f'\033[1;36m' "[3]" '\033[0;0m' " Transferência")
        print(f'\033[1;36m' "[4]" '\033[0;0m' " Configuração")
        print(f'\033[1;36m' "[5]" '\033[0;0m' " Desconectar")

        escolha = input('\n:')

        if escolha == '1':
            depositar()
        if escolha == '2':
            sacar()
        if escolha == '3':
            transferir()    
        #if escolha == '4':

        if escolha == '5':
            break
        else:
            print('Opção inválida.')
            continue

    
def depositar():
    global usuario_login
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
            cursor.execute('UPDATE usuarios SET saldo = saldo + ? WHERE login = ?', (valor_a_depositar,usuario_login))
            conn.commit()
            print(f"\nDeposito de R${valor_a_depositar} efetuado com sucesso.")
            criar_barra()
            
            print(f'\033[1;36m' "[S]" '\033[0;0m' " Depositar novamente")
            print(f'\033[1;36m' "[N]" '\033[0;0m' " Voltar")
            opçao = input('\n')
            if opçao.lower() == 'n':
                d = 'sair'
                limpar_console()
                break
            elif opçao.lower() == 's':
                limpar_console()                
            else:
                limpar_console()
                print('\nOpção inválida')
                continue
                    
def sacar():
    global usuario_login
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
            return

        elif valor_a_sacar.isalpha() or float(valor_a_sacar) == 0:
            limpar_console()
            print('\nValor inexistente! Digite um valor válido\n')
        else:
            valor_a_sacar = float(valor_a_sacar)            
            cursor.execute('SELECT saldo FROM usuarios WHERE login = ?', (usuario_login,))
            saldo = cursor.fetchone()
            
            if saldo is None:
                limpar_console()
                print('Usuário não encontrado.')
                return
            
            saldo = saldo[0]

            if valor_a_sacar > saldo:
                limpar_console()
                print(f'\033[1;31m'"Você não tem saldo suficiente para essa transação!"'\033[0;0m')

            else:                
                cursor.execute('UPDATE usuarios SET saldo = saldo - ? WHERE login = ?',(valor_a_sacar, usuario_login))
                conn.commit()
                print(f'\nSaque de R${valor_a_sacar} efetuado com sucesso!')
                criar_barra()            

                print(f'\033[1;36m' "[S]" '\033[0;0m' " Sacar novamente")
                print(f'\033[1;36m' "[N]" '\033[0;0m' " Voltar")
                opçao = input('\n').lower()
                if opçao == 'n':
                    d = 'sair'
                    limpar_console()
                    break
                elif opçao == 's':
                    limpar_console()                
                else:
                    limpar_console()
                    criar_barra()
                    print(f'\033[1;31m','\nOpção inválida', '\033[0;0m')
                    continue

def transferir():
    global usuario_login
    d = 'ficar'
    while d == 'ficar':
        limpar_console()
        print('-' * 18)
        print('|-- Transferir --|')
        print('-' * 18)        

        try:
            id = int(input('Digite o "ID" da conta bancária que deseja transferir:\n')) # Pedindo o receptor

            cursor.execute('SELECT * FROM usuarios WHERE id = ?', (id,)) # Validando se o receptor ID existe no .bd
            valida = cursor.fetchone()
            if id == 0:
                limpar_console()
                print('Voltando...')
                time.sleep(2)
                break
            elif valida is None:
                limpar_console()
                print('Cliente não encontrado! Informe o ID corretamente...')
                time.sleep(2)
                continue
        except sqlite3.Error as e:
            print(f'Cliente não encontrado. Verifique o ID e tente novamente.') # Se não existir dá erro!
            continue
        
        else:
            criar_barra()
            print('Deixe em branco para retornar.')
            criar_barra()
            valor_transferir = input('Digite o valor a ser transferido: ') # Pedindo valor para transferir

            if valor_transferir == '':
                print('Voltando...')
                time.sleep(1)
                limpar_console()
                break
            elif valor_transferir.isalpha():
                limpar_console()
                print('Opção inválida, tente digitar um valor válido!')
                time.sleep(2)
                continue            
            else:
                try:
                    cursor.execute('SELECT saldo FROM usuarios WHERE login = ?', (usuario_login,)) # Validando se há saldo
                    saldo = cursor.fetchone()
                    if float(valor_transferir) == 0:
                        limpar_console()
                        print('\033[1;31m' "Valor inválido, tente novamente!"'\033[0;0m')
                        time.sleep(2)                        
                        continue
                    elif saldo is not None and saldo[0] >= float(valor_transferir) >= 0:
                        saldo = saldo[0]
                        cursor.execute('UPDATE usuarios SET saldo = saldo - ? WHERE login = ?', (valor_transferir, usuario_login))
                        cursor.execute('UPDATE usuarios SET saldo = saldo + ? WHERE id = ?',(valor_transferir, id))
                        conn.commit()
                        limpar_console()
                        criar_barra()
                        print(f'\033[1;32m' "Transferência efetuada com sucesso!" '\033[0;0m')
                        criar_barra()
                        print(f'\033[1;36m' "[S]" '\033[0;0m' " Transferir novamente...")
                        print(f'\033[1;36m' "[N]" '\033[0;0m' " Sair...")
                        op1 = input('').lower()
                        if op1 == 's':
                            continue
                        elif op1 != 'n':
                            criar_barra()
                            print('Voltando...')
                            time.sleep(2)
                            limpar_console()
                            break
                        
                    else:
                        limpar_console()
                        criar_barra()
                        print('\033[1;31m' "Saldo é insuficiente para essa transação!"'\033[0;0m')                        
                        criar_barra()
                        e = 'ficar'
                        while e == 'ficar':                            
                            print('Deseja tentar novamente? S/N')
                            criar_barra()
                            opcao = input('').lower()
                            if opcao == 's':
                                limpar_console()
                                e = 'sair'
                            elif opcao == 'n':
                                criar_barra()
                                print('Voltando...')
                                time.sleep(2)
                                limpar_console()
                                break
                            else:
                                limpar_console()              
                                print('Opção inválida!')
                                continue
                except sqlite3.Error as e2:
                    print(f'Não foi possível fazer transferia, confira os dados novamente.{e2}')       
     
