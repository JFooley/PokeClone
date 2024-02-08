import pygame, os, copy
from pygame import Rect
from settings import * 
from battle import Battle
from utils import *
from classes import Guider

class BattleUI:
	# buttons
	BUTTON_MOVE = "BM"
	BUTTON_SIMPLE = "BS"
	BUTTON_DAO = "BD"

	def __init__(self, battleObject: Battle, game):
		self.game = game
		self.battle: Battle = battleObject
		self.clock = pygame.time.Clock()

		# Variables
		self.intro_offset = (WIDTH // 2)
		self.time_stamp = 0
		was_pressed = []
	
		# general 
		self.display_surface = pygame.display.get_surface()
		self.font_medium = pygame.font.Font(UI_FONT,UI_FONT_SIZE)

		# hp bar setup 
		self.daoA_hpbar = pygame.Rect(HP_A_POS_X, HP_A_POS_Y, HP_BAR_WIDTH, BAR_HEIGHT)
		self.daoB_hpbar = pygame.Rect(HP_B_POS_X, HP_B_POS_Y, HP_BAR_WIDTH, BAR_HEIGHT)
		self.daoA_hptext = pygame.Rect(HPTEXT_A_POS_X, HPTEXT_A_POS_Y, HP_BAR_WIDTH, BAR_HEIGHT)
		self.daoB_hptext = pygame.Rect(HPTEXT_B_POS_X, HPTEXT_B_POS_Y, HP_BAR_WIDTH, BAR_HEIGHT)

		# info text setup
		self.daoA_name = pygame.Rect(NAMETEXT_A_POS_X, NAMETEXT_A_POS_Y, HP_BAR_WIDTH, BAR_HEIGHT)
		self.daoB_name = pygame.Rect(NAMETEXT_B_POS_X, NAMETEXT_B_POS_Y, HP_BAR_WIDTH, BAR_HEIGHT)

		# initiative text setup
		self.daoA_init = pygame.Rect(INITTEXT_A_POS_X, INITTEXT_A_POS_Y, HP_BAR_WIDTH, BAR_HEIGHT)
		self.daoB_init = pygame.Rect(INITTEXT_B_POS_X, INITTEXT_B_POS_Y, HP_BAR_WIDTH, BAR_HEIGHT)

		# menu buttons setup
		self.fight_menu_up = pygame.Rect(BUTTON_UP_X, BUTTON_UP_Y, BUTTON_WIDTH, BUTTON_HEIGTH)
		self.fight_menu_down = pygame.Rect(BUTTON_DOWN_X, BUTTON_DOWN_Y, BUTTON_WIDTH, BUTTON_HEIGTH)
		self.fight_menu_left = pygame.Rect(BUTTON_LEFT_X, BUTTON_LEFT_Y, BUTTON_WIDTH, BUTTON_HEIGTH)
		self.fight_menu_right = pygame.Rect(BUTTON_RIGHT_X, BUTTON_RIGHT_Y, BUTTON_WIDTH, BUTTON_HEIGTH)

		# Summon buttons setup

		# Chat text setup
		self.chat_box = pygame.Rect(CHATBOX_POS_X, CHATBOX_POS_Y, CHATBOX_WIDTH, CHATBOX_HEIGTH)

		# Listas
		self.daos = generateDaos(archiveName= os.path.join("Data", "Daos.csv"))

	def run(self):
		keys = pygame.key.get_pressed()

		if self.battle.state == Battle.DEFAULT:
			pass
		elif self.battle.state == Battle.INTRO:
			self.play_intro()
		elif self.battle.state == Battle.END:
			self.play_ending()
		else:
			self.display()

			#### Vai para input() ####
			if self.game.state == 1 and self.battle.state == Battle.MAIN_MENU:
				if keys[pygame.K_LEFT] and not self.was_pressed[pygame.K_LEFT]:
					self.battle.state = Battle.FIGHT_MENU
				elif keys[pygame.K_RIGHT] and not self.was_pressed[pygame.K_RIGHT]:
					self.battle.state = Battle.SUMMON_MENU

			elif self.game.state == 1 and self.battle.state == Battle.FIGHT_MENU:
				####### Test #######
				if keys[pygame.K_UP] and not self.was_pressed[pygame.K_UP]:
					self.battle.state = Battle.TEXT_ON_SCREEN
				if keys[pygame.K_DOWN] and not self.was_pressed[pygame.K_DOWN]:
					self.battle.state = Battle.TEXT_ON_SCREEN
				if keys[pygame.K_LEFT] and not self.was_pressed[pygame.K_LEFT]:
					self.battle.state = Battle.TEXT_ON_SCREEN
				if keys[pygame.K_RIGHT] and not self.was_pressed[pygame.K_RIGHT]:
					self.battle.state = Battle.TEXT_ON_SCREEN
				####### Test #######
					
			elif self.game.state == 1 and self.battle.state == Battle.TEXT_ON_SCREEN:
				####### Test #######
				if keys[pygame.K_DOWN] and not self.was_pressed[pygame.K_DOWN]:
					self.battle.state = Battle.MAIN_MENU
				####### Test #######
					
			elif self.game.state == 1 and self.battle.state == Battle.SUMMON_MENU:
				####### Test #######
				if keys[pygame.K_DOWN] and not self.was_pressed[pygame.K_DOWN]:
					self.battle.state = Battle.MAIN_MENU
				####### Test #######
			#### Vai para input() ####

		####### Test ########
		if self.game.state == 0 and keys[pygame.K_SPACE] and not self.was_pressed[pygame.K_SPACE]:
			daoA1 = self.daos['3']
			daoA2 = self.daos['10']
			daoA3 = self.daos['15']
			self.game.player.Insert_dao(daoA1)
			self.game.player.Insert_dao(daoA2)
			self.game.player.Insert_dao(daoA3)

			daoB1 = self.daos['6']
			daoB2 = self.daos['20']
			daoB3 = self.daos['30']
			enemy = Guider("Enemy", 0, {}, [daoB1, daoB2, daoB3])

			self.battle.Start(self.game.player, enemy)

		if self.game.state == 1 and keys[pygame.K_UP] and not self.was_pressed[pygame.K_UP]:
			self.battle.initA += 1 
		elif self.game.state == 1 and keys[pygame.K_DOWN] and not self.was_pressed[pygame.K_DOWN]:
			self.battle.initA -= 1 if self.battle.initA > 0 else 0

		if self.game.state == 1 and keys[pygame.K_SPACE] and not self.was_pressed[pygame.K_SPACE]:
			self.battle.End()
		####### Test ######## 
		
		# Copy the keys list to check in the next frame if it was pressed
		self.was_pressed = copy.deepcopy(keys)

	def show_bar(self, current, max_amount, bg_rect, color):
		# draw bg 
		pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)

		# converting stat to pixel
		ratio = current / max_amount
		current_rect = bg_rect.copy()
		current_rect.width = bg_rect.width * ratio

		# drawing the bar
		pygame.draw.rect(self.display_surface, color, current_rect)
		# pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)

	def show_text(self, text, rect, color):
		# drawning the text
		text_surface = self.font_medium.render(text, True, color)
		self.display_surface.blit(text_surface, rect)

	def show_button(self, type, text, textcolor, rect: Rect, battle: Battle, index: int):
		# draw bg 
		pygame.draw.rect(self.display_surface, UI_BG_COLOR, rect, border_radius= int(BUTTON_HEIGTH // 2))
		
		padding_X = BUTTON_HEIGTH // 2
		padding_Y = 5
		text_offset = pygame.Rect((rect.left + padding_X), (rect.top + padding_Y), BUTTON_WIDTH, BUTTON_HEIGTH)

		# draw text
		if type == self.BUTTON_SIMPLE:
			text_surface = self.font_medium.render(text, True, textcolor)
			self.display_surface.blit(text_surface, text_offset)

		if type == self.BUTTON_MOVE:
			text_surface = self.font_medium.render(text, True, textcolor)
			self.display_surface.blit(text_surface, text_offset)

	def show_chatbox(self, text, textcolor, rect: Rect):
		# draw bg
		pygame.draw.rect(self.display_surface, UI_BG_COLOR, rect, border_radius= int(BUTTON_HEIGTH))

		# draw text
		padding_X = BUTTON_HEIGTH
		padding_Y = BUTTON_HEIGTH // 2
		text_offset = pygame.Rect((rect.left + padding_X), (rect.top + padding_Y), CHATBOX_WIDTH, CHATBOX_WIDTH)
		text_surface = self.font_medium.render(text, True, textcolor)
		self.display_surface.blit(text_surface, text_offset)

	def display(self):
		top_width = WIDTH * 5/8
		bottom_width = WIDTH * 3/8

		L1 = (0, 0)
		L2 = (top_width, 0)
		L3 = (bottom_width, HEIGTH)
		L4 = (0, HEIGTH)
		
		R1 = (WIDTH, 0)
		R2 = (top_width, 0)
		R3 = (bottom_width, HEIGTH)
		R4 = (WIDTH, HEIGTH)
		
		pygame.draw.polygon(surface= self.display_surface, color= "#4e668a", points= [L1, L2, L3])
		pygame.draw.polygon(surface= self.display_surface, color= "#4e668a", points= [L1, L3, L4])

		pygame.draw.polygon(surface= self.display_surface, color= "#854a4a", points= [R1, R2, R3])
		pygame.draw.polygon(surface= self.display_surface, color= "#854a4a", points= [R1, R3, R4])

		# Dao A
		self.show_bar(int(self.battle.currentDaoA.currentHP), int(self.battle.currentDaoA.HP), self.daoA_hpbar, HP_COLOR)
		self.show_text(f"{int(self.battle.currentDaoA.currentHP)} / {int(self.battle.currentDaoA.HP)}", self.daoA_hptext, TEXT_COLOR)
		self.show_text(f"LV: {self.battle.currentDaoA.level} {self.battle.currentDaoA.name}", self.daoA_name, TEXT_COLOR)
		self.show_text(f"+{self.battle.initA}", self.daoA_init, TEXT_COLOR)

		# Dao B
		self.show_bar(int(self.battle.currentDaoB.currentHP), int(self.battle.currentDaoB.HP), self.daoB_hpbar, HP_COLOR)
		self.show_text(f"{int(self.battle.currentDaoB.currentHP)} / {int(self.battle.currentDaoB.HP)}", self.daoB_hptext, TEXT_COLOR)
		self.show_text(f"LV: {self.battle.currentDaoB.level} {self.battle.currentDaoB.name}", self.daoB_name, TEXT_COLOR)
		self.show_text(f"+{self.battle.initB}", self.daoB_init, TEXT_COLOR)
		
		if self.battle.state == Battle.MAIN_MENU:
			self.show_button(self.BUTTON_SIMPLE, "Summon", TEXT_COLOR, self.fight_menu_right, self.battle, 0)
			self.show_button(self.BUTTON_SIMPLE, "Fight", TEXT_COLOR, self.fight_menu_left, self.battle, 0)

		elif self.battle.state == Battle.FIGHT_MENU:
			moveA = self.battle.currentDaoA.moves[0].name if 0 < len(self.battle.currentDaoA.moves) else "Move A"
			self.show_button(self.BUTTON_SIMPLE, moveA, TEXT_COLOR, self.fight_menu_up, self.battle, 0)

			moveB = self.battle.currentDaoA.moves[1].name if 0 < len(self.battle.currentDaoA.moves) else "Move B"
			self.show_button(self.BUTTON_SIMPLE, moveB, TEXT_COLOR, self.fight_menu_left, self.battle, 0)

			moveC = self.battle.currentDaoA.moves[2].name if 0 < len(self.battle.currentDaoA.moves) else "Move C"
			self.show_button(self.BUTTON_SIMPLE, moveC, TEXT_COLOR, self.fight_menu_right, self.battle, 0)

			moveD = self.battle.currentDaoA.moves[3].name if 0 < len(self.battle.currentDaoA.moves) else "Move D"
			self.show_button(self.BUTTON_SIMPLE, moveD, TEXT_COLOR, self.fight_menu_down, self.battle, 0)

		elif self.battle.state == Battle.SUMMON_MENU:
			pass # Colocar as esferas DAO 

		elif self.battle.state == Battle.TEXT_ON_SCREEN:
			# CRIAR UMA FORMA DE QUEBRAR A LINHA
			texto_teste = "Ola tudo bem? hahahhaa Ola tudo bem? hahahhaa"
			self.show_chatbox(texto_teste, TEXT_COLOR, self.chat_box)
	
	def play_intro(self):
		if self.intro_offset <= 0:
			self.battle.state = Battle.MAIN_MENU
			return
		else:
			self.intro_offset -= WIDTH * (pygame.time.Clock().tick(FPS) / 1000) 
			if self.intro_offset <= 0:
				self.intro_offset = 0

		top_width = WIDTH * 5/8
		bottom_width = WIDTH * 3/8

		L1 = (0 - self.intro_offset, 0 + self.intro_offset)
		L2 = (top_width  - self.intro_offset, 0 + self.intro_offset)
		L3 = (bottom_width - self.intro_offset, HEIGTH + self.intro_offset)
		L4 = (0 - self.intro_offset, HEIGTH + self.intro_offset)
		
		R1 = (WIDTH + self.intro_offset, 0 - self.intro_offset)
		R2 = (top_width + self.intro_offset, 0 - self.intro_offset)
		R3 = (bottom_width + self.intro_offset, HEIGTH - self.intro_offset)
		R4 = (WIDTH + self.intro_offset, HEIGTH - self.intro_offset)
		
		pygame.draw.polygon(surface= self.display_surface, color= "#4e668a", points= [L1, L2, L3])
		pygame.draw.polygon(surface= self.display_surface, color= "#4e668a", points= [L1, L3, L4])

		pygame.draw.polygon(surface= self.display_surface, color= "#854a4a", points= [R1, R2, R3])
		pygame.draw.polygon(surface= self.display_surface, color= "#854a4a", points= [R1, R3, R4])

	def play_ending(self):
		self.display_surface.fill("black")

		if self.intro_offset == WIDTH // 2:
			self.battle.state = Battle.DEFAULT
			return
		else:
			self.intro_offset += WIDTH * (pygame.time.Clock().tick(FPS) / 1000) 
			if self.intro_offset >= WIDTH // 2:
				self.intro_offset = WIDTH // 2

		top_width = WIDTH * 5/8
		bottom_width = WIDTH * 3/8

		L1 = (0 - self.intro_offset, 0 + self.intro_offset)
		L2 = (top_width  - self.intro_offset, 0 + self.intro_offset)
		L3 = (bottom_width - self.intro_offset, HEIGTH + self.intro_offset)
		L4 = (0 - self.intro_offset, HEIGTH + self.intro_offset)
		
		R1 = (WIDTH + self.intro_offset, 0 - self.intro_offset)
		R2 = (top_width + self.intro_offset, 0 - self.intro_offset)
		R3 = (bottom_width + self.intro_offset, HEIGTH - self.intro_offset)
		R4 = (WIDTH + self.intro_offset, HEIGTH - self.intro_offset)
		
		pygame.draw.polygon(surface= self.display_surface, color= "#4e668a", points= [L1, L2, L3])
		pygame.draw.polygon(surface= self.display_surface, color= "#4e668a", points= [L1, L3, L4])

		pygame.draw.polygon(surface= self.display_surface, color= "#854a4a", points= [R1, R2, R3])
		pygame.draw.polygon(surface= self.display_surface, color= "#854a4a", points= [R1, R3, R4])

