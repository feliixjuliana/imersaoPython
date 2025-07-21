cont = 0
lista = []

while cont < 5:
    numero = int(input("Informe um número"))
    lista.append(numero)
    cont+=1

for i in lista:
    if(i % 2 == 0):
        print(f"{i} é par")
    else:
        print(f"{i} não é par")
