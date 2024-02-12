import pygame
from pygame import Rect

class Dao:
	IDLE = 0
	PRE_MAGIC = 1
	POST_MAGIC = 2
	PRE_PHYSICAL = 4
	POST_PHYSICAL = 5
	GET_HIT = 6
	CRITICAL_GET_HIT = 7
	DEFEATED = 8

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
		self.current_frame = 0
		self.on_screen = False

	def addEffect(self, effect):
		pass

	def applyEffect(self):
		pass
      
	def clearEffect(self):
		self.effects.clear()

	def set_sprits(self):
		from utils import find_images_paths
		base_path = "Assets/daos/" + self.id + "/"
		
		# IDLE
		self.sprites[self.IDLE] = []
		idle_paths = find_images_paths(base_path, "idle")
		for path in idle_paths:
			sprite = pygame.image.load(path)
			self.sprites[self.IDLE].append(sprite)

		# PRE MAGIC
		self.sprites[self.PRE_MAGIC] = []
		idle_paths = find_images_paths(base_path, "pre_magic")
		for path in idle_paths:
			sprite = pygame.image.load(path)
			self.sprites[self.IDLE].append(sprite)

		# POST MAGIC
		self.sprites[self.POST_MAGIC] = []
		idle_paths = find_images_paths(base_path, "post_magic")
		for path in idle_paths:
			sprite = pygame.image.load(path)
			self.sprites[self.IDLE].append(sprite)

		# PRE PHYSICAL
		self.sprites[self.PRE_PHYSICAL] = []
		idle_paths = find_images_paths(base_path, "pret_physical")
		for path in idle_paths:
			sprite = pygame.image.load(path)
			self.sprites[self.IDLE].append(sprite)

		# POST PHYSICAL
		self.sprites[self.POST_PHYSICAL] = []
		idle_paths = find_images_paths(base_path, "post_physical")
		for path in idle_paths:
			sprite = pygame.image.load(path)
			self.sprites[self.IDLE].append(sprite)

		# GET HIT
		self.sprites[self.GET_HIT] = []
		idle_paths = find_images_paths(base_path, "get_hit")
		for path in idle_paths:
			sprite = pygame.image.load(path)
			self.sprites[self.IDLE].append(sprite)
		
		# CRITICAL GET HIT
		self.sprites[self.CRITICAL_GET_HIT] = []
		idle_paths = find_images_paths(base_path, "critical_get_hit")
		for path in idle_paths:
			sprite = pygame.image.load(path)
			self.sprites[self.IDLE].append(sprite)
		
		# DEFEATED
		self.sprites[self.DEFEATED] = []
		idle_paths = find_images_paths(base_path, "defeated")
		for path in idle_paths:
			sprite = pygame.image.load(path)
			self.sprites[self.IDLE].append(sprite)

	def show_dao(self, surface, pos_X, pos_Y, side= "A"):
		if self.on_screen == True:
			if self.state == self.IDLE:
				sprite = self.sprites[self.IDLE][self.current_frame]
				width, heigth = sprite.get_size()
				if side == "B":
					sprite = pygame.transform.flip(sprite, True, False)
				surface.blit(sprite, (pos_X - (width // 2), pos_Y - (heigth // 2)))
				self.current_frame = self.current_frame + 1 if (self.current_frame + 1) < len(self.sprites[self.IDLE]) else 0
			
			elif self.state == self.PRE_MAGIC:
				sprite = self.sprites[self.PRE_MAGIC][self.current_frame]
				width, heigth = sprite.get_size()
				if side == "B":
					sprite = pygame.transform.flip(sprite, True, False)
				surface.blit(sprite, (pos_X - (width // 2), pos_Y - (heigth // 2)))
				self.current_frame += 1 if (self.current_frame + 1) < len(self.sprites[self.PRE_MAGIC]) else 0

			elif self.state == self.POST_MAGIC:
				sprite = self.sprites[self.POST_MAGIC][self.current_frame]
				width, heigth = sprite.get_size()
				if side == "B":
					sprite = pygame.transform.flip(sprite, True, False)
				surface.blit(sprite, (pos_X - (width // 2), pos_Y - (heigth // 2)))
				self.current_frame += 1 if (self.current_frame + 1) < len(self.sprites[self.POST_MAGIC]) else 0
								
			elif self.state == self.PRE_PHYSICAL:
				sprite = self.sprites[self.PRE_PHYSICAL][self.current_frame]
				width, heigth = sprite.get_size()
				if side == "B":
					sprite = pygame.transform.flip(sprite, True, False)
				surface.blit(sprite, (pos_X - (width // 2), pos_Y - (heigth // 2)))
				self.current_frame += 1 if (self.current_frame + 1) < len(self.sprites[self.PRE_PHYSICAL]) else 0
								
			elif self.state == self.POST_PHYSICAL:
				sprite = self.sprites[self.POST_PHYSICAL][self.current_frame]
				width, heigth = sprite.get_size()
				if side == "B":
					sprite = pygame.transform.flip(sprite, True, False)
				surface.blit(sprite, (pos_X - (width // 2), pos_Y - (heigth // 2)))
				self.current_frame += 1 if (self.current_frame + 1) < len(self.sprites[self.POST_PHYSICAL]) else 0
								
			elif self.state == self.GET_HIT:
				sprite = self.sprites[self.GET_HIT][self.current_frame]
				width, heigth = sprite.get_size()
				if side == "B":
					sprite = pygame.transform.flip(sprite, True, False)
				surface.blit(sprite, (pos_X - (width // 2), pos_Y - (heigth // 2)))
				self.current_frame += 1 if (self.current_frame + 1) < len(self.sprites[self.GET_HIT]) else 0
								
			elif self.state == self.CRITICAL_GET_HIT:
				sprite = self.sprites[self.CRITICAL_GET_HIT][self.current_frame]
				width, heigth = sprite.get_size()
				if side == "B":
					sprite = pygame.transform.flip(sprite, True, False)
				surface.blit(sprite, (pos_X - (width // 2), pos_Y - (heigth // 2)))
				self.current_frame += 1 if (self.current_frame + 1) < len(self.sprites[self.CRITICAL_GET_HIT]) else 0
								
			elif self.state == self.DEFEATED:
				sprite = self.sprites[self.DEFEATED][self.current_frame]
				width, heigth = sprite.get_size()
				if side == "B":
					sprite = pygame.transform.flip(sprite, True, False)
				surface.blit(sprite, (pos_X - (width // 2), pos_Y - (heigth // 2)))
				self.current_frame += 1 if (self.current_frame + 1) < len(self.sprites[self.DEFEATED]) else 0

class Effect:
	EMPTY = "empty"

class Move:
	def __init__(self, id, name, text, type, kind, power: int, accuracy: float, uses: int, level: int, effect= ""):
		self.id = id
		self.name = name
		self.text = text
		self.type = type 
		self.kind = kind
		self.base_power = power
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

