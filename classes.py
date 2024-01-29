class Move:
    def __init__(self, id: int, name, effect, type, kind, power: int, accuracy: float, pp: int):
        self.id = id
        self.name = name
        self.effect = effect
        self.type = type
        self.kind = kind
        self.power = power
        self.accuracy = accuracy
        self.pp = pp

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
	def __init__(self, id, name, level: int, type1, type2, STR: int, POW: int, RES: int, MRES: int, AGI: int, HP: int, currentHP: int, effect: list):
		self.id = id
		self.name = name
		self.level = level
		self.type1 = type1
		self.type2 = type2
		
		self.HP = HP
		self.STR = STR
		self.RES = RES
		self.POW = POW
		self.MRES = MRES
		self.AGI = AGI
		
		self.curretHP = currentHP
		self.effect = effect
		
class Effect: 
	def __init__(self, type, HP, STR, RES, POW, MRES, AGI, INIT: int, foeHP, foeSTR, foeRES, foePOW, foeMRES, foeAGI, foeINIT: int):
		self.type = type
		
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
		