print("Informe os três ângulos do triângulo:")
angulo1 = float(input("Ângulo 1: "))
angulo2 = float(input("Ângulo 2: "))
angulo3 = float(input("Ângulo 3: "))

if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
    print("O triângulo é Retângulo (possui um ângulo reto = 90°).")
elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
    print("O triângulo é Obtusângulo (possui um ângulo obtuso (maior que 90°).")
elif angulo1 < 90 or angulo2 < 90 or angulo3 < 90:
    print("O triângulo é Acutângulo (possui todos os ângulos agudos (menores que 90°).")
else:
    print("Valores inválidos, refaça")