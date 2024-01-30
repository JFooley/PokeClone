import random
from classes import Move, Pokemon, Dao, Effect

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
    RateA = pokeA.speed * moveA.accuracy * (1 + (initA * 0.25))
    RateB = pokeB.speed * moveB.accuracy * (1 + (initB * 0.25))

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
    
def daoDuel(daoA: Dao, daoB: Dao, moveA: int, moveB: int, initA, initB):
    RateA = daoA.AGI * daoA.moves[moveA].accuracy * (1 + (initA * 0.25))
    RateB = daoB.AGI * daoB.moves[moveB].accuracy * (1 + (initB * 0.25))

    ratePool = RateA + RateB + ((RateA + RateB) / 2)

    ResultRNG = random.uniform(0, ratePool)
    
    print("-" * 100)
    print(f"{daoA.name}: {RateA} ({(RateA * 100) // ratePool}%)")
    print("-- VS --")
    print(f"{daoB.name}: {RateB} ({(RateB * 100) // ratePool}%)")
    print("-" * 100)

    if ResultRNG < RateA:
        return "A"
    elif ResultRNG < (RateA + RateB):
        return "B"
    else:
        return "D"
    
def daoDamage(atacker: Dao, defender: Dao, move: Move, effeChart: dict, level: int):
    # Calcular o critico
    CRIT = 2.0 if random.uniform(0, 100) < 6.25 else 1.0

    # Check the Same Type Atack Bonus (STAB)
    STAB = 1.5 if move.type == atacker.type1 or move.type == defender.type2 else 1.0

    # Check move type and return the damage
    if move.kind == "Physical":
        damage = (((level + 5)/125) * (atacker.STR/defender.RES) * move.power * STAB * CRIT * float(effeChart[move.type][defender.type1]) * float(effeChart[move.type][defender.type2] if defender.type2 else 1))
        return int(round(damage))
    
    elif move.kind == "Special":
        damage = (((level + 5)/125) * (atacker.POW /defender.MRES) * move.power * STAB * CRIT * float(effeChart[move.type][defender.type1]) * float(effeChart[move.type][defender.type2] if defender.type2 else 1)) 
        return int(round(damage))
    
    else:
        return 0
