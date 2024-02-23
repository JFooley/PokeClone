from animation import Animation
from settings import ANIM_FPS_IDLE, ANIM_FPS_PRE_MAGIC, ANIM_FPS_POST_MAGIC, ANIM_FPS_PRE_PHYSICAL, ANIM_FPS_POST_PHYSICAL, ANIM_FPS_GET_HIT, ANIM_FPS_CRITICAL_GET_HIT, ANIM_FPS_DEFEATED

class Dao:
	IDLE = 0
	PRE_MAGIC = 1
	POST_MAGIC = 2
	PRE_PHYSICAL = 3
	POST_PHYSICAL = 4
	GET_HIT = 5
	CRITICAL_GET_HIT = 6
	DEFEATED = 7

	def __init__(self, id, name, level: int, type1, type2, moves: list, STR: int, RES: int, POW: int, MRES: int, AGI: int, HP: int, currentHP: int, summon_text= f"Eu invoco você!"):
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
		self.summon_text = summon_text
            
		self.state = self.IDLE

		self.sprites = {}
		self.on_screen = False

	def addEffect(self, effect):
		pass

	def applyEffect(self):
		pass
      
	def clearEffect(self):
		self.effects.clear()

	def set_sprits(self):
		base_path = "Assets/daos/" + self.id + "/"
		
		# IDLE
		IDLE_anim = Animation(ANIM_FPS_IDLE)
		IDLE_anim.set_images(base_path + "idle", "idle")
		self.sprites[self.IDLE] = IDLE_anim

		# PRE_MAGIC
		PRE_MAGIC_anim = Animation(ANIM_FPS_PRE_MAGIC)
		PRE_MAGIC_anim.set_images(base_path + "pre_magic", "pre_magic")
		self.sprites[self.PRE_MAGIC] = PRE_MAGIC_anim
				
		# POST_MAGIC
		POST_MAGIC_anim = Animation(ANIM_FPS_POST_MAGIC)
		POST_MAGIC_anim.set_images(base_path + "post_magic", "post_magic")
		self.sprites[self.POST_MAGIC] = POST_MAGIC_anim
				
		# PRE_PHYSICAL
		PRE_PHYSICAL_anim = Animation(ANIM_FPS_PRE_PHYSICAL)
		PRE_PHYSICAL_anim.set_images(base_path + "pre_physical", "pre_physical")
		self.sprites[self.PRE_PHYSICAL] = PRE_PHYSICAL_anim
				
		# POST_PHYSICAL
		POST_PHYSICAL_anim = Animation(ANIM_FPS_POST_PHYSICAL)
		POST_PHYSICAL_anim.set_images(base_path + "post_physical", "post_physical")
		self.sprites[self.POST_PHYSICAL] = POST_PHYSICAL_anim
				
		# GET_HIT
		GET_HIT_anim = Animation(ANIM_FPS_GET_HIT)
		GET_HIT_anim.set_images(base_path + "get_hit", "get_hit")
		self.sprites[self.GET_HIT] = GET_HIT_anim
				
		# CRITICAL_GET_HIT
		CRITICAL_GET_HIT_anim = Animation(ANIM_FPS_CRITICAL_GET_HIT)
		CRITICAL_GET_HIT_anim.set_images(base_path + "critical_get_hit", "critical_get_hit")
		self.sprites[self.CRITICAL_GET_HIT] = CRITICAL_GET_HIT_anim
				
		# DEFEATED
		DEFEATED_anim = Animation(ANIM_FPS_DEFEATED)
		DEFEATED_anim.set_images(base_path + "defeated", "defeated")
		self.sprites[self.DEFEATED] = DEFEATED_anim

	def unset_sprits(self):
		self.sprites.clear()

	def show_dao(self, surface, pos_X, pos_Y, side= "A", size= None):
		if self.on_screen == True:
			if self.currentHP <= 0:
				self.state = self.DEFEATED
			elif self.state == self.DEFEATED:
				self.state = self.IDLE

			if self.state == self.IDLE:
				self.sprites[self.IDLE].play(surface, pos_X, pos_Y, mirrored= False if side == "A" else True, size= size)
							
			elif self.state == self.PRE_MAGIC:
				self.sprites[self.PRE_MAGIC].play(surface, pos_X, pos_Y, mirrored= False if side == "A" else True, size= size)

			elif self.state == self.POST_MAGIC:
				self.sprites[self.POST_MAGIC].play_once(surface, pos_X, pos_Y, mirrored= False if side == "A" else True, size= size)
				if self.sprites[self.POST_MAGIC].is_playing == False:
					self.state = self.IDLE
			
			elif self.state == self.PRE_PHYSICAL:
				self.sprites[self.PRE_PHYSICAL].play(surface, pos_X, pos_Y, mirrored= False if side == "A" else True, size= size)
			
			elif self.state == self.POST_PHYSICAL:
				self.sprites[self.POST_PHYSICAL].play_once(surface, pos_X, pos_Y, mirrored= False if side == "A" else True, size= size)
				if self.sprites[self.POST_PHYSICAL].is_playing == False:
					self.state = self.IDLE

			elif self.state == self.GET_HIT:
				self.sprites[self.GET_HIT].play_once(surface, pos_X, pos_Y, mirrored= False if side == "A" else True, size= size)
				if self.sprites[self.GET_HIT].is_playing == False:
					self.state = self.IDLE

			elif self.state == self.CRITICAL_GET_HIT:
				self.sprites[self.CRITICAL_GET_HIT].play_once(surface, pos_X, pos_Y, mirrored= False if side == "A" else True, size= size)
				if self.sprites[self.CRITICAL_GET_HIT].is_playing == False:
					self.state = self.IDLE

			elif self.state == self.DEFEATED:
				self.sprites[self.DEFEATED].play(surface, pos_X, pos_Y, mirrored= False if side == "A" else True, size= size)

class Move:
	PHYSICAL = "Physical"
	SPECIAL = "Special"

	def __init__(self, id, name, text, type, kind, power: int, accuracy: float, uses: int, level: int, effect= ""):
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

