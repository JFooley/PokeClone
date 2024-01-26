import os
from Classes import *

chatlog = ''
# Simulação de batalha
while True:
    os.system("cls")
    
    vidaP1 = (personagem1.vida_atual * 100) // personagem1.vida
    barravidaP1 = vidaP1 * "[" if personagem1.vida_atual > 0  else 'Desmaiado'

    vidaP2 = (personagem2.vida_atual * 100) // personagem2.vida
    barravidaP2 = vidaP2 * "[" if personagem2.vida_atual > 0  else 'Desmaiado'

    print(f"{personagem1.nome}: {personagem1.vida_atual}/{personagem1.vida} \n {barravidaP1}")
    print(f"{personagem2.nome}: {personagem2.vida_atual}/{personagem2.vida} \n {barravidaP2}")

    print(chatlog)
    chatlog = ""

    if personagem1.vida_atual <= 0:
        print(f"\n {personagem1.nome} foi derrotado! ")
        break
    if personagem2.vida_atual <= 0:
        print(f"\n {personagem2.nome} foi derrotado!")
        break

    atkP1 = int(input(f"Qual ataque o {personagem1.nome} deve usar? ")) -1
    atkP2 = int(input(f"Qual ataque o {personagem2.nome} deve usar? ")) -1

    if personagem1.velocidade > personagem2.velocidade:
        chatlog += personagem1.realizar_ataque(personagem2, atkP1)
        chatlog += personagem2.realizar_ataque(personagem1, atkP2)

    else:
        chatlog += personagem2.realizar_ataque(personagem1, atkP2)
        chatlog += personagem1.realizar_ataque(personagem2, atkP1)


input()
