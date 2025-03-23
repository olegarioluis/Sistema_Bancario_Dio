import os

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu).lower()

    if opcao == "d":

        os.system('clear')
        print('Deposito\n')
        deposito = float(input('Digite o valor a ser Depositado: '))

        if deposito > 0:
            saldo += deposito
            dados = f'\nDeposito feito no Valor de R${deposito:.2f}'
            extrato += dados
            os.system('clear')
            print(dados)

        else:
            print("Operação falhou!! O valor informado é inválido.")


    elif opcao == "s":

        os.system('clear')
        print("Saque\n")

        limite_saque = numero_saque >= LIMITE_SAQUE

        while True:
            saque = float(input("Digite um Valor para o saque: "))

            if saque > saldo:
                os.system('clear')
                print('Você não tem saldo suficiente para realizar o saque.')

            else:
                break

        if saque > limite:
            os.system('clear')
            print('Você só pode fazer um saque ate R$500.00')

        elif limite_saque:
            os.system('clear')
            print('Limite de saques diários ja realizados.')


        elif saque > 0:
            saldo -= saque
            informacao = f'\nSaque feito no valor de R${saque}.'
            extrato += informacao
            os.system('clear')
            print(informacao)
            numero_saque += 1

        else:
            os.system('clear')
            print("A operação Falhou!! Tente novamente.")

    elif opcao == "e":

        os.system('clear')
        print("Extrato")
        if not extrato:
            print('Sem Depósitos ou Saques')
        else:
            extrato
        print(extrato)
        print(f"\nVocê tem R${saldo} de Saldo.")

    elif opcao == "q":
        break

    else:
        print("Operação Inválida, Por favor Selecione novamente a operação desejada.")