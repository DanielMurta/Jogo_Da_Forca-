import random
from Palavras import Palavras

Palavra = random.choice(Palavras)
letras_descobertas = []
tentativas = 4
acertou = False

while True:
    for letra in Palavra:
        if letra in letras_descobertas:
            print(letra, end=" ")
        else:
            print("_", end=" ")

    print("")  
    print("")  
    resposta = input("Escolha uma letra: ").lower().strip()
    letras_descobertas.append(resposta)
    if resposta not in Palavra:
        tentativas -= 1
        if tentativas != 0:
            print(f"Voce agora possuiu {tentativas} tentativas!")

    acertou = True
    for letra in Palavra:
        if letra not in letras_descobertas:
            acertou = False

    if tentativas == 0 or acertou:
        break

if acertou:
    print("Parabéns, você acertou a palavra!")
else:
    print(f"Você perdeu, a palavra era {Palavra}")

    
