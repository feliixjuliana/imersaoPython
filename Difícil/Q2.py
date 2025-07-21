#Esse código usa o join para evidenciar o local que a letra está, caso não fez com essa opção, apenas retire o join.
import random

palavrasSec = ["casa", "sofá", "janela"]
palavraSecreta = random.choice(palavrasSec)
adivinhadas = ["_"] * len(palavraSecreta)
tentativas = 8

print(f"Bem-vindo ao Jogo de Adivinhação de Palavras!\nAdivinhe a palavra. Ela tem {len(palavraSecreta)} letras.\nVocê tem {tentativas} tentativas.\nPalavra atual: {' '.join(adivinhadas)}")

while tentativas > 0:
    entradaJogador = input("Digite uma letra ou a palavra inteira: ").lower()

    if not entradaJogador.isalpha():
        print("Entrada inválida. Por favor, digite apenas letras.")
    elif len(entradaJogador) > 1:
        if entradaJogador == palavraSecreta:
            print(f"Parabéns! Você adivinhou a palavra '{palavraSecreta}'!")
            break
        else:
            print("Palavra incorreta. Você perde uma tentativa.")
            tentativas -= 1
    else:
        letra = entradaJogador
        if letra in palavraSecreta:
            print(f"Boa! A letra '{letra}' está na palavra.")
            for i in range(len(palavraSecreta)):
                if palavraSecreta[i] == letra:
                    adivinhadas[i] = letra
        else:
            print(f"A letra '{letra}' não está na palavra. Você perde uma tentativa.")
            tentativas -= 1

    print(f"Palavra atual: {' '.join(adivinhadas)}\nTentativas restantes: {tentativas}")

    if "_" not in adivinhadas:
        print(f"Você adivinhou a palavra '{palavraSecreta}'!")
        break

print(f"Suas tentativas acabaram!\nA palavra secreta era: '{palavraSecreta}'\nMais sorte na próxima vez!")