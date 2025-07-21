frase = input("Me informe a frase: ")

#Se formos assumir que não terá acentos
vogaisDeclaradas = "aeiou"

#Se formos assumir que terá acentos ficará semelhante a linha abaixo. Não coloquei todos, pois é exemplo.
#vogaisDeclaradas = "aeiouáàéãíêó"

contVogais = 0
contConsoantes = 0

for i in frase:
    if i in vogaisDeclaradas:
        contVogais += 1
    elif i != " ":
        contConsoantes += 1

print(f"Temos de consoantes: {contConsoantes} \n Temos de vogais: {contVogais}")

#Coloquei o  i != " ", pois se deixarmos só o else os espaços serão contados. É importante evidenciar que tem que ser diferente deles.