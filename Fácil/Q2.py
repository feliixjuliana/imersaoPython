palavraEscolhida = input("Informe uma palavra: ")

while palavraEscolhida != "sair":
    print(palavraEscolhida[:: -1])
    palavraEscolhida = input("Informe uma palavra: ")

print("Programa encerrado")