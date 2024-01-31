import copy

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

class Dao:
	def __init__(self, id, name, level: int, type1, type2, moves: list, STR: int, RES: int, POW: int, MRES: int, AGI: int, HP: int, currentHP: int):
		self.id = id
		self.name = name
		self.level = level
		self.type1 = type1
		self.type2 = type2
		self.moves = moves
		
		self.HP = HP
		self.STR = STR
		self.RES = RES
		self.POW = POW
		self.MRES = MRES
		self.AGI = AGI
		
		self.currentHP = currentHP
		self.effects: list = []
            
		self.state = "idle"
	
	def checkEffects(self):
		condition = []
		for effect in self.effects:
			if effect.type != Effect.DEFAULT and effect.type != Effect.CONTINOUS:
				condition.append(effect.type)

		return condition
			
class Effect: 
	DEFAULT = "default"
	POISON = "poison"
	FREEZE = "freeze"
	FRAGILE = "fragile"
	CONTINOUS = "continuous effect"

	def __init__(self, type, HP, STR, RES, POW, MRES, AGI, INIT: int, foeHP, foeSTR, foeRES, foePOW, foeMRES, foeAGI, foeINIT: int):
		self.type = type if type != '' else Effect.DEFAULT
		self.turn = 0

		self.HP = HP
		self.STR = STR
		self.RES = RES
		self.POW = POW
		self.MRES = MRES
		self.AGI = AGI
		self.INIT = INIT

		self.foeHP = foeHP
		self.foeSTR = foeSTR
		self.foeRES = foeRES
		self.foePOW = foePOW
		self.foeMRES = foeMRES
		self.foeAGI = foeAGI
		self.foeINIT = foeINIT
	
	def applyStats(self, dao: Dao, foe: Dao):
		dao.HP += (self.HP * dao.HP) // 100
		dao.currentHP += (self.HP * dao.HP) // 100
		dao.STR += (self.STR * dao.STR) // 100
		dao.POW += (self.POW * dao.POW) // 100
		dao.RES += (self.RES * dao.RES) // 100
		dao.MRES += (self.MRES * dao.MRES) // 100
		dao.AGI += (self.AGI * dao.AGI) // 100

		foe.HP += (self.foeHP * foe.HP) // 100
		foe.currentHP += (self.foeHP * foe.HP) // 100
		foe.STR += (self.foeSTR * foe.STR) // 100
		foe.POW += (self.foePOW * foe.POW) // 100
		foe.RES += (self.foeRES * foe.RES) // 100
		foe.MRES += (self.foeMRES * foe.MRES) // 100
		foe.AGI += (self.foeAGI * foe.AGI) // 100

		return dao, foe
	
	def applyInit(self, init, foeInit):
		init += self.INIT
		foeInit += self.foeINIT

		return init, foeInit
	
class Move:
	def __init__(self, id, name, text, type, kind, power: int, accuracy: float, uses: int, level: int, effect: list):
		self.id = id
		self.name = name
		self.text = text
		self.type = type 
		self.kind = kind
		self.power = power
		self.accuracy = accuracy
		self.uses = uses
		self.level = level
		self.effect = effect