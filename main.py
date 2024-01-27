import csv
import os
from classes import Move, Pokemon
from battle import moveDamage, duel

def generateMoves(archiveName: str):
    moveChart = {}
    with open(archiveName, 'r') as File:
        result = csv.reader(File)
        for line in result:
            move = Move(int(line[0]), line[1], line[2], line[3], line[4], int(line[5]), float(line[6]), int(line[7]))
            moveChart[line[1]] = move
            moveChart[line[0]] = move
    
    return moveChart

def generatePokemons(archiveName: str):
    pokemonChart = {}
    with open(archiveName, 'r') as File:
        result = csv.reader(File)
        for line in result:
            poke = Pokemon(line[0], line[1], line[2], line[3], int(line[4]), int(line[5]), int(line[6]), int(line[7]), int(line[8]), int(line[9]), int(line[10]), int(line[11]), bool(line[12]), [])
            pokemonChart[line[0]] = poke
    
    return pokemonChart

def generateEffectiveness(archiveName: str):
    effectivenessChart = {}

    with open(archiveName, 'r') as File:
        result = csv.reader(File)
        for line in result:
            effectivenessChart[line[0]] = {
                'Normal' : float(line[1]), 
                'Fire' : float(line[2]), 
                'Water' : float(line[3]), 
                'Electric' : float(line[4]), 
                'Grass' : float(line[5]), 
                'Ice' : float(line[6]), 
                'Fighting' : float(line[7]), 
                'Poison' : float(line[8]), 
                'Ground' : float(line[9]), 
                'Flying' : float(line[10]), 
                'Psychic' : float(line[11]), 
                'Bug' : float(line[12]), 
                'Rock' : float(line[13]), 
                'Ghost' : float(line[14]), 
                'Dragon' : float(line[15]), 
                'Dark' : float(line[16]), 
                'Steel' : float(line[17]), 
                'Fairy' : float(line[18])
                }
    
    return effectivenessChart


def main():
    moves = {}
    pokemons = {}
    effectiveness = {}

    moves = generateMoves("Moves.csv") 
    pokemons = generatePokemons("Pokemons.csv") 
    effectiveness = generateEffectiveness("Effectiveness.csv")

    # Testes
    IDpokeA = input("Insira o número do pokemon A: ")
    LVpokeA = int(input("Insira o nivel do pokemom A: "))
    IDpokeB = input("Insira o número do pokemon B: ")
    LVpokeB = int(input("Insira o nivel do pokemon B: "))

    pokeA: Pokemon = pokemons[IDpokeA]
    pokeB: Pokemon = pokemons[IDpokeB]

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

        duelResult = duel(pokeA, pokeB, moveA, moveB, initA, initB)

        if duelResult == "A":
            initB += 1
            damage = moveDamage(pokeA, pokeB, moveA, effectiveness, LVpokeA)
            vidaB = (vidaB - damage) if (vidaB - damage > 0) else 0
            print(f"{pokeA.name} atacou {pokeB.name} utilizando {moveA.name}, causando {damage} de dano!")

        elif duelResult == "B":
            initA += 1
            damage = moveDamage(pokeB, pokeA, moveB, effectiveness, LVpokeB)
            vidaA = (vidaA - damage) if (vidaA - damage > 0) else 0
            print(f"{pokeB.name} atacou {pokeA.name} utilizando {moveB.name}, causando {damage} de dano!")

        elif duelResult == "D":
            damageA = moveDamage(pokeA, pokeB, moveA, effectiveness, LVpokeA)
            damageB = moveDamage(pokeB, pokeA, moveB, effectiveness, LVpokeB)

            vidaA = (vidaA - damageB) if (vidaA - damageB > 0) else 0
            vidaB = (vidaB - damageA) if (vidaB - damageA > 0) else 0

            print(f"{pokeA.name} atacou {pokeB.name} utilizando {moveA.name}, causando {damageA} de dano!")
            print(f"Que devolveu o ataque utilizando {moveB.name}, causando {damageB} de dano em {pokeA.name}!")

main()