import random
from classes import Move, Dao, Guider
from settings import WIDTH
import copy

class Battle():
    # Terms
    YOU = "A"
    FOE = "B"
    ACTION_SUMMON = "summon"
    ACTION_BATTLE = "move"

    # States
    DEFAULT = 'default'
    INTRO = 'itr'
    MAIN_MENU = 'mmn'
    FIGHT_MENU = 'fgt'
    SUMMON_MENU = 'smn'
    TEXT_ON_SCREEN = 'txt'
    PRE_DUEL = "prdu"
    POST_DUEL = "podu"
    END = 'end'


    def __init__(self):
        self.guiderA = None
        self.guiderB = None
        self.originalListA: list = []
        self.originalListB: list = []
        self.battleListA: list = []
        self.battleListB: list = []
        
        self.currentDaoA: Dao = None
        self.currentDaoB: Dao = None

        self.initA: int
        self.initB: int

        self.state = self.DEFAULT

    def Start(self, guiderA: Guider, guiderB: Guider):
        if self.state == self.DEFAULT:
            self.originalListA = guiderA.daos_list
            self.originalListB = guiderB.daos_list

            self.battleListA = copy.deepcopy(guiderA.daos_list)
            self.battleListB = copy.deepcopy(guiderB.daos_list)

            self.currentDaoA: Dao = self.battleListA[0]
            self.currentDaoB: Dao = self.battleListB[0]

            self.initA = 0
            self.initB = 0

            for daoA in self.battleListA:
                daoA.set_sprits()
                daoA.on_screen = True
            for daoB in self.battleListB:
                daoB.set_sprits()
                daoB.on_screen = True

            self.state = Battle.INTRO

    def End(self):
        for daoA in self.battleListA:
            daoA.unset_sprits()
            daoA.on_screen = False
        for daoB in self.battleListB:
            daoB.set_sprits()
            daoB.on_screen = False

        self.state = Battle.END

    def Turn(self, actionA, actionB, action_index_A, action_index_B):
        # Check the actions
        if actionA == self.ACTION_SUMMON and actionB == self.ACTION_SUMMON: # Both summon
            self.Summon(self.YOU, action_index_A)
            self.Summon(self.FOE, action_index_B)

        elif actionA == self.ACTION_SUMMON and actionB == self.ACTION_BATTLE: # You summon, foe battle
            self.Summon(self.YOU, action_index_A)
            emptyMove = Move()

        elif actionA == self.ACTION_BATTLE and actionB == self.ACTION_SUMMON: # You battle, foe summon
            self.Summon(self.FOE, action_index_B)
            emptyMove = Move()

        elif actionA == self.ACTION_BATTLE and actionB == self.ACTION_BATTLE:
            emptyMove = Move()
            emptyMove = Move()

        # Apply effects
    
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

        if ResultRNG < RateA:
            return "A"
        elif ResultRNG < (RateA + RateB):
            return "B"
        else:
            return "D"
        
    def Damage(self, atacker: Dao, defender: Dao, move: Move, effeChart: dict):
        # Random crit hit
        CRIT = 2.0 if random.uniform(0, 100) < 6.25 else 1.0

        # Check the Same Type Atack Bonus (STAB)
        STAB = 1.5 if move.type == atacker.type1 or move.type == defender.type2 else 1.0

        # Check move type and return the damage
        if move.kind == "Physical":
            damage = (((atacker.level + 5)/125) * (atacker.STR/defender.RES) * move.power * STAB * CRIT * float(effeChart[move.type][defender.type1]) * float(effeChart[move.type][defender.type2] if defender.type2 else 1) + 2)
            return int(round(damage))
        
        elif move.kind == "Special":
            damage = (((atacker.level + 5)/125) * (atacker.POW /defender.MRES) * move.power * STAB * CRIT * float(effeChart[move.type][defender.type1]) * float(effeChart[move.type][defender.type2] if defender.type2 else 1) + 2) 
            return int(round(damage))
        
        else:
            return 0
        
