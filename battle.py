import random
from classes import Move, Pokemon, Dao, Effect
import copy

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
    
class Battle():
    YOU = "A"
    FOE = "B"
    SUMMON = "summon"

    def __init__(self, daoListA: list, daoListB: list):
        # Copia a lista de daos para a batalha
        self.battleListA: list = copy.deepcopy(daoListA)
        self.battleListB: list = copy.deepcopy(daoListB)

        self.currentDaoA: Dao = None
        self.currentDaoB: Dao = None

        self.initA: int
        self.initB: int

    def Start(self):
        self.currentDaoA: Dao = self.battleListA[0]
        self.currentDaoB: Dao = self.battleListB[0]

        self.initA = 0
        self.initB = 0

    def Turn(self, actionA, actionB): # Action can be SUMMON or a number from 0 to 3 (move index)
        # Check the actions
        if actionA == self.SUMMON and actionB == self.SUMMON: # Both summon
            self.Summon(self.YOU, actionA)
            self.Summon(self.FOE, actionB)

        elif actionA == self.SUMMON and actionB != self.SUMMON: # You summon, foe battle
            self.Summon(self.YOU, actionA)
            emptyMove = Move()

        elif actionA != self.SUMMON and actionB == self.SUMMON: # You battle, foe summon
            self.Summon(self.FOE, actionB)
            emptyMove = Move()

        else: # Both battle
            pass

        # Apply your effects
        remainingEffects = []
        for effect in self.currentDaoA.effects:
            effect.applyInit(self.initA, self.initB)
            effect.applyStats(self.currentDaoA, self.currentDaoB)
            effect.turn += 1

            # Treat continous effects
            if effect.type == Effect.FREEZE and effect.turn >= 2:
                continue # Removes the freeze effect in the 2° turn
            elif effect.type == Effect.POISON and effect.turn >= 5:
                continue # Removes the poison effect in the 5° turn
            elif effect.type == Effect.CONTINOUS or effect.type == Effect.FREEZE or effect.type == Effect.POISON:
                remainingEffects.append(effect)
        else: # Finally
            self.currentDaoA.effects = copy.deepcopy(remainingEffects)
            remainingEffects.clear

        # Apply foe effects
        for effect in self.currentDaoB.effects:
            effect.applyInit(self.initB, self.initA)
            effect.applyStats(self.currentDaoB, self.currentDaoA)
            effect.turn += 1

            # Treat continous effects
            if effect.type == Effect.FREEZE and effect.turn >= 2:
                continue # Removes the freeze effect in the 2° turn
            elif effect.type == Effect.POISON and effect.turn >= 5:
                continue # Removes the poison effect in the 5° turn
            if effect.type == Effect.CONTINOUS or effect.type == Effect.FREEZE or effect.type == Effect.POISON:
                remainingEffects.append(effect)
        else: # Finally
            self.currentDaoB.effects = copy.deepcopy(remainingEffects)
            remainingEffects.clear
    
    def Summon(self, guider, daoIndex: int):
        if guider == Battle.YOU:
            self.battleListA.insert(0, self.battleListA.pop(daoIndex))
            self.currentDaoA = self.battleListA[0]
        else:
            self.battleListB.insert(0, self.battleListB.pop(daoIndex))
            self.currentDaoB = self.battleListB[0]

    def Duel(self, moveA: Move, moveB: Move):
        # Calcula o rate de acerto individual e total
        RateA = self.currentDaoA.AGI * moveA.accuracy * (1 + (self.initA * 0.25))
        RateB = self.currentDaoB.AGI * moveB.accuracy * (1 + (self.initB * 0.25))
        ratePool = RateA + RateB + ((RateA + RateB) / 2)

        # Escolhe o numero que define quem ganha
        ResultRNG = random.uniform(0, ratePool)
        
        print("-" * 100)
        print(f"{self.currentDaoA.name}: {(RateA // 100)} ({(RateA * 100) // ratePool}%)")
        print("-- VS --")
        print(f"{self.currentDaoB.name}: {(RateB // 100)} ({(RateB * 100) // ratePool}%)")
        print("-" * 100)

        if ResultRNG < RateA:
            return "A"
        elif ResultRNG < (RateA + RateB):
            return "B"
        else:
            return "D"
        
    def Damage(self, atacker: Dao, defender: Dao, move: Move, effeChart: dict):
        # Random crit hit
        CRIT = 2.0 if random.uniform(0, 100) < 6.25 else 1.0

        # Check fragile
        for effect in atacker.effects:
            if effect.type == Effect.FRAGILE:
                CRIT = 2.0

        # Check the Same Type Atack Bonus (STAB)
        STAB = 1.5 if move.type == atacker.type1 or move.type == defender.type2 else 1.0

        # Check move type and return the damage
        if move.kind == "Physical":
            damage = (((atacker.level + 5)/125) * (atacker.STR/defender.RES) * move.power * STAB * CRIT * float(effeChart[move.type][defender.type1]) * float(effeChart[move.type][defender.type2] if defender.type2 else 1))
            return int(round(damage))
        
        elif move.kind == "Special":
            damage = (((atacker.level + 5)/125) * (atacker.POW /defender.MRES) * move.power * STAB * CRIT * float(effeChart[move.type][defender.type1]) * float(effeChart[move.type][defender.type2] if defender.type2 else 1)) 
            return int(round(damage))
        
        else:
            return 0
        
