import csv
from classes import Move, Pokemon, Dao

def generateMoves(archiveName: str):
    moveChart = {}
    with open(archiveName, 'r') as File:
        result = csv.reader(File)
        for line in result:
            move = Move(line[0], line[1], line[2], line[3], line[4], int(line[5]), float(line[6]), uses= 0, level= 1, effect=[])
            moveChart[line[1]] = move
            moveChart[line[0]] = move
    
    return moveChart

def getMove(archiveName: str, ID):
    with open(archiveName, 'r') as File:
        result = csv.reader(File)
        for line in result:
            if line[0] == ID:
                selectedMove = Move(line[0], line[1], line[2], line[3], line[4], int(line[5]), float(line[6]), uses= 0, level= 1, effect=[])
    
    return selectedMove

def generateDaos(archiveName: str):
    daoChart = {}
    with open(archiveName, 'r') as File:
        result = csv.reader(File)
        for line in result:
            daoObj = Dao(id= line[0], name= line[1], level= 1, type1= line[2], type2= line[3], moves= [], STR= int(line[6]), RES= int(line[7]), POW= int(line[8]), MRES= int(line[9]), AGI= int(line[10]), HP= int(line[5]), currentHP= int(line[5]))
            daoChart[line[0]] = daoObj

    return daoChart

def getDao(archiveName: str, ID):
    with open(archiveName, 'r') as File:
        result = csv.reader(File)
        for line in result:
            if line[0] == ID:
                selectedDao = Dao(id= line[0], name= line[1], level= 1, type1= line[2], type2= line[3], moves= [], STR= int(line[6]), RES= int(line[7]), POW= int(line[8]), MRES= int(line[9]), AGI= int(line[10]), HP= int(line[5]), currentHP= int(line[5]))
    
    return selectedDao

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