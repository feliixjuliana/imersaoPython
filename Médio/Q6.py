dddCapitais = {
    82: "Maceió",
    71: "Salvador",
    85: "Fortaleza",
    98: "São Luís",
    83: "João Pessoa",
    81: "Recife",
    86: "Teresina",
    84: "Natal",
    79: "Aracaju"
}

ddd_informado = int(input("Digite o código de DDD (ex: 81): "))

if ddd_informado in dddCapitais:
    capital = dddCapitais[ddd_informado]
    print(f"O DDD {ddd_informado} pertence à capital: {capital}")
    #Caso queira, pode fazer diretamente no print, ou seja, print(f"O DDD {ddd_informado} pertence à capital: {dddCapitais[ddd_informado]}"), nesse caso, não precisará da variável capital.
else:
    print(f"O DDD {ddd_informado} não corresponde a uma capital do Nordeste em nosso registro.")
