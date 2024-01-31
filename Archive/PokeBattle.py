import random 
import csv

class Move:
	def __init__(self, id, name, text, type, kind, power: int, accuracy: float):
		self.id = id
		self.name = name
		self.text = text
		self.type = type 
		self.kind = kind
		self.power = power
		self.accuracy = accuracy
          
class Pokemon:
    def __init__(self, id, name, type1, type2, total: int, hp: int, attack: int, defense: int, spAtk: int, spDef: int, speed: int, generation: int, legendary: bool, moves: list):
        self.id = id
        self.name = name
        self.type1 = type1
        self.type2 = type2
        
        self.total = total
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.spAtk = spAtk
        self.spDef = spDef
        self.speed = speed
        
        self.generation = generation
        self.legendary = legendary
        self.moves = moves

def pokeDamage(atacker: Pokemon, defender: Pokemon, move: Move, effeChart: dict, level: int):
    # Calcular o critico
    CRIT = 2.0 if random.uniform(0, 100) < 6.25 else 1.0

    # Check the Same Type Atack Bonus (STAB)
    STAB = 1.5 if move.type == atacker.type1 or move.type == defender.type2 else 1.0

    # Check move type and return the damage
    if move.kind == "Physical":
        damage = (((level + 5)/125) * (atacker.attack/defender.defense) * move.power * STAB * CRIT * float(effeChart[move.type][defender.type1]) * float(effeChart[move.type][defender.type2] if defender.type2 else 1))
        return int(round(damage))
    
    elif move.kind == "Special":
        damage = (((level + 5)/125) * (atacker.spAtk /defender.spDef) * move.power * STAB * CRIT * float(effeChart[move.type][defender.type1]) * float(effeChart[move.type][defender.type2] if defender.type2 else 1)) 
        return int(round(damage))
    
    else:
        return 0
    
def pokeDuel(pokeA: Pokemon, pokeB: Pokemon, moveA: Move, moveB: Move, initA, initB):
    # Calcula o rate de acerto individual e total
    RateA = pokeA.speed * moveA.accuracy * (1 + (initA * 0.25))
    RateB = pokeB.speed * moveB.accuracy * (1 + (initB * 0.25))

    # Escolhe o numero que define quem ganha
    ratePool = RateA + RateB + ((RateA + RateB) / 2)

    ResultRNG = random.uniform(0, ratePool)
    
    print("-" * 100)
    print(f"{pokeA.name}: {(RateA * 100) // ratePool}%")
    print("-- VS --")
    print(f"{pokeB.name}: {(RateB * 100) // ratePool}%")
    print("-" * 100)

    if ResultRNG < RateA:
        return "A"
    elif ResultRNG < (RateA + RateB):
        return "B"
    else:
        return "D"
    
def generatePokemons(archiveName: str):
    pokemonChart = {}
    with open(archiveName, 'r') as File:
        result = csv.reader(File)
        for line in result:
            poke = Pokemon(line[0], line[1], line[2], line[3], int(line[4]), int(line[5]), int(line[6]), int(line[7]), int(line[8]), int(line[9]), int(line[10]), int(line[11]), bool(line[12]), [])
            pokemonChart[line[0]] = poke
    
    return pokemonChart

def getPokemon(archiveName: str, ID):
    with open(archiveName, 'r') as File:
        result = csv.reader(File)
        for line in result:
            if line[0] == ID:
                selectedPoke = Pokemon(line[0], line[1], line[2], line[3], int(line[4]), int(line[5]), int(line[6]), int(line[7]), int(line[8]), int(line[9]), int(line[10]), int(line[11]), bool(line[12]), [])
    
    return selectedPoke

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

def generateMoves(archiveName: str):
    moveChart = {}
    with open(archiveName, 'r') as File:
        result = csv.reader(File)
        for line in result:
            move = Move(line[0], line[1], line[2], line[3], line[4], int(line[5]), float(line[6]), uses= 0, level= 1, effect=[])
            moveChart[line[1]] = move
            moveChart[line[0]] = move
    
    return moveChart