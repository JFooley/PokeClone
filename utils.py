import csv, random
from classes import Dao, Move

def generateMoves(archiveName: str):
    moveChart = {}
    with open(archiveName, 'r') as File:
        result = csv.reader(File)
        for line in result:
            move = Move(line[0], line[1], line[2], line[3], line[4], int(line[5]), float(line[6]), uses= 0, level= 1)
            moveChart[line[1]] = move
            moveChart[line[0]] = move
    
    return moveChart

def getMove(archiveName: str, ID):
    with open(archiveName, 'r') as File:
        result = csv.reader(File)
        for line in result:
            if line[0] == ID:
                selectedMove = Move(line[0], line[1], line[2], line[3], line[4], int(line[5]), float(line[6]), uses= 0, level= 1)
    
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

def generateTypeChart(archiveName: str):
    typeChart = {}

    with open(archiveName, 'r') as File:
        result = csv.reader(File)
        for line in result:
            typeChart[line[0]] = {
                'Fire' : float(line[1]),
                'Water' : float(line[2]),
                'Earth' : float(line[3]),
                'Air' : float(line[4]),
                'Thunder' : float(line[5]),
                'Light' : float(line[6]),
                'Darkness' : float(line[7]),
                'Bestial' : float(line[8]),
                'Ethereal' : float(line[9]),
                'Machine' : float(line[10]),
                'Undead' : float(line[11]),
                }
    
    return typeChart

def generateColorChart(archiveName: str):
    typeChart = {}

    with open(archiveName, 'r') as File:
        result = csv.reader(File)
        for line in result:
            typeChart[line[0]] = line[1]
    
    return typeChart

def generateRandomDao(archiveName, level= 1):
    pass

def generateRandomMove(archiveName, type= "default"):
    move_chart = generateMoves(archiveName)

    if type == "default":
        move_list = list(move_chart.values())
        return random.choice(move_list)
    
    else:
        same_type_list = []
        for move in move_chart.values():
            if move.type == type:
                same_type_list.append(move)

        return random.choice(same_type_list)