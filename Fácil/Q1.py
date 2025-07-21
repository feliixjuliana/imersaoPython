saldoMedio = float(input("Informe seu saldo médio: "))

if saldoMedio > 400:
    credito = (saldoMedio * 30)/100
    saldoFinal = credito + saldoMedio
    print(f"Seu saldo médio é: R${saldoMedio}\n O valor do seu crédito é: R${credito:.2f}\n Seu saldo final fica: R${saldoFinal}")

elif saldoMedio >= 300 and saldoMedio <= 400:
    credito = (saldoMedio * 25)/100
    saldoFinal = credito + saldoMedio
    print(f"Seu saldo médio é: R${saldoMedio}\n O valor do seu crédito é: R${credito:.2f}\n Seu saldo final fica: R${saldoFinal}")

elif saldoMedio >= 200 and saldoMedio < 300:
    credito = (saldoMedio * 20)/100
    saldoFinal = credito + saldoMedio
    print(f"Seu saldo médio é: R${saldoMedio}\n O valor do seu crédito é: R${credito:.2f}\n Seu saldo final fica: R${saldoFinal}")

else:
    credito = (saldoMedio * 10)/100
    saldoFinal = credito + saldoMedio
    print(f"Seu saldo médio é: R${saldoMedio}\n O valor do seu crédito é: R${credito:.2f}\n Seu saldo final fica: R${saldoFinal}")