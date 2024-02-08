import os
from battle import *
from utils import *

def main():
    moves = generateMoves(os.path.join("Data", "Moves.csv")) 
    effectiveness = generateEffectiveness(os.path.join("Data", "Effectiveness.csv"))

    IDpokeA = input("Insira o número do pokemon A: ")
    LVpokeA = int(input("Insira o nivel do pokemom A: "))
    IDpokeB = input("Insira o número do pokemon B: ")
    LVpokeB = int(input("Insira o nivel do pokemon B: "))

    pokeA: Pokemon = getPokemon(archiveName= os.path.join("Data", "Pokemons.csv"), ID= IDpokeA)
    pokeB: Pokemon = getPokemon(archiveName= os.path.join("Data", "Pokemons.csv"), ID= IDpokeB)

    initA = 0
    initB = 0

    vidaA = pokeA.hp
    vidaB = pokeB.hp

    while True:
        vidaP1 = (vidaA * 100) // pokeA.hp
        barravidaP1 = vidaP1 * "[" if vidaA > 0  else 'Desmaiado'

        vidaP2 = (vidaB * 100) // pokeB.hp
        barravidaP2 = vidaP2 * "[" if vidaB > 0  else 'Desmaiado'

        print(f"\n{pokeA.name} (LV: {LVpokeA}): {vidaA}/{pokeA.hp} \n {barravidaP1}")
        print(f"{pokeB.name} (LV: {LVpokeB}): {vidaB}/{pokeB.hp} \n {barravidaP2}")

        if vidaA <= 0 or vidaB <= 0:
            break

        inputA = input(f"O que {pokeA.name} deve fazer? ")
        inputB = input(f"O que {pokeB.name} deve fazer? ")

        os.system("cls")

        moveA: Move = moves[inputA]
        moveB: Move = moves[inputB]

        duelResult = pokeDuel(pokeA, pokeB, moveA, moveB, initA, initB)

        if duelResult == "A":
            initB += 1
            damage = pokeDamage(pokeA, pokeB, moveA, effectiveness, LVpokeA)
            vidaB = (vidaB - damage) if (vidaB - damage > 0) else 0
            print(f"{pokeA.name} atacou {pokeB.name} utilizando {moveA.name}, causando {damage} de dano!")

        elif duelResult == "B":
            initA += 1
            damage = pokeDamage(pokeB, pokeA, moveB, effectiveness, LVpokeB)
            vidaA = (vidaA - damage) if (vidaA - damage > 0) else 0
            print(f"{pokeB.name} atacou {pokeA.name} utilizando {moveB.name}, causando {damage} de dano!")

        elif duelResult == "D":
            damageA = pokeDamage(pokeA, pokeB, moveA, effectiveness, LVpokeA)
            damageB = pokeDamage(pokeB, pokeA, moveB, effectiveness, LVpokeB)

            vidaA = (vidaA - damageB) if (vidaA - damageB > 0) else 0
            vidaB = (vidaB - damageA) if (vidaB - damageA > 0) else 0

            print(f"{pokeA.name} atacou {pokeB.name} utilizando {moveA.name}, causando {damageA} de dano!")
            print(f"Que devolveu o ataque utilizando {moveB.name}, causando {damageB} de dano em {pokeA.name}!")

main()