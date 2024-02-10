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

class  Guider:
    def __init__(self, name, level, inventory: dict, daos_list: list):
        self.name = name
        self.level = level
        self.inventory = inventory
        self.daos_list = daos_list if daos_list != None else []

    def Raise_level(self):
        self.level += 1

    def Insert_dao(self, dao: Dao):
        self.daos_list.append(dao)

    def Generate_daos(self, archiveName,  daos_ID_list):
        from utils import getDao
        for ID in daos_ID_list:
            single_dao = getDao(archiveName= archiveName, ID= ID)
            self.daos_list.append(single_dao)