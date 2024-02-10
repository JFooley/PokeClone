import pygame, os, copy
from pygame import Rect
from settings import * 
from battle import Battle
from utils import *
from classes import Guider
from input import Input

class BattleUI:
	def __init__(self, battleObject: Battle, game):
		self.game = game
		self.battle: Battle = battleObject
		self.clock = pygame.time.Clock()
 
		# Variables
		self.intro_offset = (WIDTH // 2)
		self.time_stamp = 0
		self.on_screen_text = ''
	
		# general 
		self.display_surface = pygame.display.get_surface()
		self.font_medium = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

		# hp bar setup 
		self.daoA_hpbar = pygame.Rect(HP_A_POS_X, HP_A_POS_Y, HP_BAR_WIDTH, BAR_HEIGHT)
		self.daoB_hpbar = pygame.Rect(HP_B_POS_X, HP_B_POS_Y, HP_BAR_WIDTH, BAR_HEIGHT)
		self.daoA_hptext = pygame.Rect(HPTEXT_A_POS_X, HPTEXT_A_POS_Y, HP_BAR_WIDTH, BAR_HEIGHT)
		self.daoB_hptext = pygame.Rect(HPTEXT_B_POS_X, HPTEXT_B_POS_Y, HP_BAR_WIDTH, BAR_HEIGHT)
		self.daoA_hpsize = 0
		self.daoB_hpsize = 0

		# info text setup
		self.daoA_name = pygame.Rect(NAMETEXT_A_POS_X, NAMETEXT_A_POS_Y, HP_BAR_WIDTH, BAR_HEIGHT)
		self.daoB_name = pygame.Rect(NAMETEXT_B_POS_X, NAMETEXT_B_POS_Y, HP_BAR_WIDTH, BAR_HEIGHT)

		# initiative text setup
		self.daoA_init = pygame.Rect(INITTEXT_A_POS_X, INITTEXT_A_POS_Y, HP_BAR_WIDTH, BAR_HEIGHT)
		self.daoB_init = pygame.Rect(INITTEXT_B_POS_X, INITTEXT_B_POS_Y, HP_BAR_WIDTH, BAR_HEIGHT)

		# buttons setup
		self.button_rect_Y = pygame.Rect(BUTTON_BANNER_Y_X, BUTTON_BANNER_Y_Y, BUTTON_WIDTH, BUTTON_HEIGTH)
		self.button_rect_A = pygame.Rect(BUTTON_BANNER_A_X, BUTTON_BANNER_A_Y, BUTTON_WIDTH, BUTTON_HEIGTH)
		self.button_rect_X = pygame.Rect(BUTTON_BANNER_X_X, BUTTON_BANNER_X_Y, BUTTON_WIDTH, BUTTON_HEIGTH)
		self.button_rect_B = pygame.Rect(BUTTON_BANNER_B_X, BUTTON_BANNER_B_Y, BUTTON_WIDTH, BUTTON_HEIGTH)

		self.button_rect_L = pygame.Rect(BUTTON_BANNER_L_X, BUTTON_BANNER_L_Y, BUTTON_WIDTH, BUTTON_HEIGTH)
		self.button_rect_R = pygame.Rect(BUTTON_BANNER_R_X, BUTTON_BANNER_R_Y, BUTTON_WIDTH, BUTTON_HEIGTH)

		# Listas
		self.daos = generateDaos(archiveName= os.path.join("Data", "Daos.csv"))

	def run(self):
		if self.battle.state == Battle.INTRO:
			self.play_intro()
		elif self.battle.state == Battle.END:
			self.play_ending()
		elif self.battle.state != Battle.DEFAULT:
			self.display()
		
		self.do_behaviour()

	def do_behaviour(self):
		if self.battle.state != Battle.DEFAULT and self.battle.state != Battle.INTRO and self.battle.state != Battle.END:
			# MAIN MENU
			if self.game.state == 1 and self.battle.state == Battle.MAIN_MENU:
				if Input().key_down(key_code= Input().X):
					self.battle.state = Battle.FIGHT_MENU
				elif Input().key_down(key_code= Input().B):
					self.battle.state = Battle.SUMMON_MENU

			# BATTLE MENU
			elif self.game.state == 1 and self.battle.state == Battle.FIGHT_MENU:
				if Input().key_down(key_code= Input().Y): 
					self.on_screen_text = "Move Y utilizado!"
					self.battle.state = Battle.TEXT_ON_SCREEN
				if Input().key_down(key_code= Input().A):
					self.on_screen_text = "Move A utilizado!"
					self.battle.state = Battle.TEXT_ON_SCREEN
				if Input().key_down(key_code= Input().X):
					self.on_screen_text = "Move X utilizado!"
					self.battle.state = Battle.TEXT_ON_SCREEN
				if Input().key_down(key_code= Input().B):
					self.on_screen_text = "Move B utilizado!"
					self.battle.state = Battle.TEXT_ON_SCREEN
					
			# TEXT ON SCREEN
			elif self.game.state == 1 and self.battle.state == Battle.TEXT_ON_SCREEN:
				if Input().key_down(key_code= Input().A):
					self.on_screen_text = ''
					self.battle.state = Battle.MAIN_MENU
			
			# SUMMON MENU
			elif self.game.state == 1 and self.battle.state == Battle.SUMMON_MENU:
				if Input().key_down(key_code= Input().Y):
					self.battle.state = Battle.TEXT_ON_SCREEN
				if Input().key_down(key_code= Input().A):
					self.battle.state = Battle.TEXT_ON_SCREEN
				if Input().key_down(key_code= Input().X):
					self.battle.state = Battle.TEXT_ON_SCREEN
				if Input().key_down(key_code= Input().B):
					self.battle.state = Battle.TEXT_ON_SCREEN
				if Input().key_down(key_code= Input().L):
					self.battle.state = Battle.TEXT_ON_SCREEN
				if Input().key_down(key_code= Input().R):
					self.battle.state = Battle.TEXT_ON_SCREEN


		### PROVISÓRIO ###
		if self.game.state == 0 and Input().key_down(key_code= Input().start):
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

		elif self.game.state == 1 and Input().key_down(key_code= Input().start):
			self.battle.End()

		if self.game.state == 1 and Input().key_down(key_code= Input().up):
			self.battle.currentDaoA.currentHP += 30
		elif self.game.state == 1 and Input().key_down(key_code= Input().down):
			self.battle.currentDaoA.currentHP -= 45
		### PROVISÓRIO ###

	def show_bar(self, current, max_amount, shadow_value, bg_rect: Rect, color, shadow_color):
		# draw bg 
		pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

		# converting stat to pixel
		ratio_curret = max(0, min(current / max_amount, 1))
		ratio_shadow = max(0, min(shadow_value / max_amount, 1))
		current_rect = bg_rect.copy()
		shadow_rect = bg_rect.copy()
		current_rect.width = bg_rect.width * ratio_curret
		shadow_rect.width = bg_rect.width * ratio_shadow

		# drawing the bar
		pygame.draw.rect(self.display_surface, shadow_color, shadow_rect)
		pygame.draw.rect(self.display_surface, color, current_rect)

	def show_text(self, text, rect, color):
		# drawning the text
		text_surface = self.font_medium.render(text, True, color)
		self.display_surface.blit(text_surface, rect)

	def show_button(self, text, textcolor, rect: Rect, l_radius, r_radius):
		# draw bg 
		pygame.draw.rect(self.display_surface, UI_BG_COLOR, rect, 
				   border_top_left_radius= l_radius, 
				   border_bottom_left_radius= l_radius,
				   border_top_right_radius= r_radius,
				   border_bottom_right_radius= r_radius)
		
		# Text offset
		text_surface = self.font_medium.render(text, True, textcolor)

		padding_X = text_surface.get_rect().width // 2
		padding_Y = text_surface.get_rect().height // 2
		
		text_rect = pygame.Rect((rect.centerx - padding_X), (rect.centery - padding_Y), BUTTON_WIDTH, BUTTON_HEIGTH)

		# draw text
		self.display_surface.blit(text_surface, text_rect)

	def show_button_UI(self, text, color, pos_X, pos_Y, l_radius, r_radius):
		rect = pygame.Rect(pos_X, pos_Y, BUTTON_HEIGTH, BUTTON_HEIGTH)

		# Draw bg
		pygame.draw.rect(self.display_surface, color, rect,
			border_top_left_radius= l_radius, 
			border_bottom_left_radius= l_radius, 
			border_top_right_radius= r_radius, 
			border_bottom_right_radius= r_radius)
		
		# Text offset
		text_surface = self.font_medium.render(text, True, UI_BG_COLOR)

		padding_X = text_surface.get_rect().width // 2
		padding_Y = text_surface.get_rect().height // 2
		
		text_rect = pygame.Rect((rect.centerx - padding_X), (rect.centery - padding_Y), BUTTON_HEIGTH, BUTTON_HEIGTH)

		# draw text
		self.display_surface.blit(text_surface, text_rect)

	def show_chatbox(self, textcolor):
		# draw bg and button
		rect = pygame.Rect(CHATBOX_POS_X, CHATBOX_POS_Y, CHATBOX_WIDTH, CHATBOX_HEIGTH)
		pygame.draw.rect(self.display_surface, UI_BG_COLOR, rect, border_radius= int(HALF_UNIT))
		self.show_button_UI("A", ABXY_COLOR, CHATBOX_BUTTON_X, CHATBOX_BUTTON_Y, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)

		# text offset
		text_surface = self.font_medium.render(self.on_screen_text, True, textcolor)

		padding_X = HALF_UNIT
		padding_Y = HALF_UNIT
		
		text_rect = pygame.Rect((rect.left + padding_X), (rect.top + padding_Y), CHATBOX_WIDTH, CHATBOX_WIDTH)

		# draw text
		self.display_surface.blit(text_surface, text_rect)

	def display(self):
		# Background
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

		# Life bars
		self.daoA_hpsize = self.daoA_hpsize + (self.battle.currentDaoA.currentHP - self.daoA_hpsize) * (0.05)
		self.show_bar(int(self.battle.currentDaoA.currentHP), int(self.battle.currentDaoA.HP), self.daoA_hpsize, self.daoA_hpbar, HP_COLOR, HP_SHADOW_COLOR)
		self.show_text(f"{int(self.battle.currentDaoA.currentHP)} / {int(self.battle.currentDaoA.HP)}", self.daoA_hptext, TEXT_COLOR)
		self.show_text(f"LV: {self.battle.currentDaoA.level} {self.battle.currentDaoA.name}", self.daoA_name, TEXT_COLOR)
		self.show_text(f"+{self.battle.initA}", self.daoA_init, TEXT_COLOR)

		self.daoB_hpsize = self.daoB_hpsize + (self.battle.currentDaoB.currentHP - self.daoB_hpsize) * (0.05)
		self.show_bar(int(self.battle.currentDaoB.currentHP), int(self.battle.currentDaoB.HP), self.daoB_hpsize, self.daoB_hpbar, HP_COLOR, HP_SHADOW_COLOR)
		self.show_text(f"{int(self.battle.currentDaoB.currentHP)} / {int(self.battle.currentDaoB.HP)}", self.daoB_hptext, TEXT_COLOR)
		self.show_text(f"LV: {self.battle.currentDaoB.level} {self.battle.currentDaoB.name}", self.daoB_name, TEXT_COLOR)
		self.show_text(f"+{self.battle.initB}", self.daoB_init, TEXT_COLOR)

		# Situacional UI
		if self.battle.state == Battle.MAIN_MENU:
			self.show_button_UI("B", ABXY_COLOR, BUTTON_B_X, BUTTON_B_Y, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)
			self.show_button_UI("X", ABXY_COLOR, BUTTON_X_X, BUTTON_X_Y, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)

			self.show_button("Summon", TEXT_COLOR, self.button_rect_B, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)
			self.show_button("Fight", TEXT_COLOR, self.button_rect_X, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)

		elif self.battle.state == Battle.FIGHT_MENU:
			self.show_button_UI("A", ABXY_COLOR, BUTTON_A_X, BUTTON_A_Y, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)
			self.show_button_UI("B", ABXY_COLOR, BUTTON_B_X, BUTTON_B_Y, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)
			self.show_button_UI("X", ABXY_COLOR, BUTTON_X_X, BUTTON_X_Y, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)
			self.show_button_UI("Y", ABXY_COLOR, BUTTON_Y_X, BUTTON_Y_Y, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)
			
			moveY = self.battle.currentDaoA.moves[0].name if 0 < len(self.battle.currentDaoA.moves) else "Move Y"
			self.show_button(moveY, TEXT_COLOR, self.button_rect_Y, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)

			moveX = self.battle.currentDaoA.moves[1].name if 0 < len(self.battle.currentDaoA.moves) else "Move X"
			self.show_button(moveX, TEXT_COLOR, self.button_rect_X, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)

			moveB = self.battle.currentDaoA.moves[2].name if 0 < len(self.battle.currentDaoA.moves) else "Move B"
			self.show_button(moveB, TEXT_COLOR, self.button_rect_B, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)

			moveA = self.battle.currentDaoA.moves[3].name if 0 < len(self.battle.currentDaoA.moves) else "Move A"
			self.show_button(moveA, TEXT_COLOR, self.button_rect_A, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)

		elif self.battle.state == Battle.SUMMON_MENU:
			dao_A = f"LV:{self.battle.battleListA[0].level} {self.battle.battleListA[0].name}" if len(self.battle.battleListA) > 0 else ""
			self.show_button_UI("A", ABXY_COLOR, BUTTON_A_X, BUTTON_A_Y, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)
			self.show_button(dao_A, TEXT_COLOR, self.button_rect_A, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)

			dao_B = f"LV:{self.battle.battleListA[1].level} {self.battle.battleListA[1].name}" if len(self.battle.battleListA) > 1 else ""
			self.show_button(dao_B, TEXT_COLOR, self.button_rect_B, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)
			self.show_button_UI("B", ABXY_COLOR, BUTTON_B_X, BUTTON_B_Y, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)

			dao_X = f"LV:{self.battle.battleListA[2].level} {self.battle.battleListA[2].name}" if len(self.battle.battleListA) > 2 else ""
			self.show_button(dao_X, TEXT_COLOR, self.button_rect_X, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)
			self.show_button_UI("X", ABXY_COLOR, BUTTON_X_X, BUTTON_X_Y, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)

			dao_Y = f"LV:{self.battle.battleListA[3].level} {self.battle.battleListA[3].name}" if len(self.battle.battleListA) > 3 else ""
			self.show_button(dao_Y, TEXT_COLOR, self.button_rect_Y, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)
			self.show_button_UI("Y", ABXY_COLOR, BUTTON_Y_X, BUTTON_Y_Y, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)

			dao_L = f"LV:{self.battle.battleListA[4].level} {self.battle.battleListA[4].name}" if len(self.battle.battleListA) > 4 else ""
			self.show_button(dao_L, TEXT_COLOR, self.button_rect_L, BUTTON_ABXY_RADIUS, 0)
			self.show_button_UI("L", ABXY_COLOR, BUTTON_L_X, BUTTON_L_Y, 0, BUTTON_ABXY_RADIUS)

			dao_R = f"LV:{self.battle.battleListA[5].level} {self.battle.battleListA[5].name}" if len(self.battle.battleListA) > 5 else ""
			self.show_button(dao_R, TEXT_COLOR, self.button_rect_R, 0, BUTTON_ABXY_RADIUS)
			self.show_button_UI("R", ABXY_COLOR, BUTTON_R_X, BUTTON_R_Y, BUTTON_ABXY_RADIUS, 0)

		elif self.battle.state == Battle.TEXT_ON_SCREEN:
			self.show_chatbox(TEXT_COLOR)
	
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

