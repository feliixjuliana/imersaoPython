saldo = 1000.00

while True:
    print("Opções: \n1. Ver Saldo\n2. Fazer Depósito\n3. Fazer Saque\n4. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        print(f"Seu saldo atual é: R$ {saldo:.2f}")
    elif escolha == '2':
        valor_deposito = float(input("Informe o valor a depositar: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso. \nNovo saldo: R$ {saldo:.2f}")
        else:
            print("Valor de depósito inválido. Por favor, digite um número positivo.")
    elif escolha == '3':
        valor_saque = float(input("Informe o valor a sacar: R$ "))
        if valor_saque <= 0:
            print("Valor de saque inválido. Por favor, digite um número positivo.")
        elif valor_saque > saldo:
            print(f"Saldo insuficiente. Seu saldo é de R$ {saldo:.2f}.")
        else:
            saldo -= valor_saque
            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.\nNovo saldo: R$ {saldo:.2f}")
    elif escolha == '4':
        print("Obrigado por usar nosso caixa eletrônico. Volte sempre!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
        
#Nessa atividade é recomendado vocês usarem try e except, mas como não demos em aula, recomendo que pesquisem. Basicamente é essencial para tratamento de erro.