#opção 1, sem armazenar

cardapio = {
    "suco": 5.50,
    "coxinha":4.00,
    "pastel": 10.50
}

print(cardapio)
escolha = input("O que deseja pedir? ")
print(f"O valor é R${cardapio[escolha]}.")

#opção 2, armazenando

"""
contaTotal = 0

while escolha != "sair": 
    contaTotal += cardapio[escolha]
    escolha = input("O que deseja pedir? ")


print(contaTotal)
"""