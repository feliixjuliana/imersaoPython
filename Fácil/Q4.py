numero = int(input("Informe o número: "))

if numero % 3 == 0 and numero % 5 ==0:
    print("FizzBuzz")
elif numero % 3 == 0:
    print("Fizz")
elif numero % 5 == 0:
    print("Buzz")
else:
    print("Não é múltiplo de 3 ou 5")