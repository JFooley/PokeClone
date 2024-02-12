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