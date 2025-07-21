custoFabrica = float(input("Informe o custo de fábrica do carro (em R$): "))

valorFinal = 0

if 0 <= custoFabrica <= 35000:
    porcDist = (custoFabrica * 5)/100
    valorFinal = custoFabrica + porcDist
    print(f"O custo total será R${valorFinal}")
elif 35000 < custoFabrica <= 70000:
    porcDist = (custoFabrica * 10)/100
    porcImp = (custoFabrica * 15)/100
    valorFinal = custoFabrica + porcDist + porcImp
    print(f"O custo total será R${valorFinal}")
elif custoFabrica > 70000:
    porcDist = (custoFabrica * 15)/100
    porcImp = (custoFabrica * 20)/100
    valorFinal = custoFabrica + porcDist + porcImp
    print(f"O custo total será R${valorFinal}")
else:
    print("Custo de fábrica inválido. Por favor, insira um valor positivo.")

