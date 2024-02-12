import pygame, os
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

		# Charts
		self.colorChart = generateColorChart("Data/ColorChart.csv")
		self.typeChart = generateTypeChart("Data/TypeChart.csv")
	
		# general 
		self.display_surface = pygame.display.get_surface()
		self.font_medium = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
		self.font_type = pygame.font.Font(UI_FONT, TYPE_FONT_SIZE)

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
		self.moves = generateMoves(archiveName= os.path.join("Data", "Moves.csv"))

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
				if Input().key_up(key_code= Input().X) and self.battle.currentDaoA.currentHP > 0:
					self.battle.state = Battle.FIGHT_MENU
				elif Input().key_up(key_code= Input().B):
					self.battle.state = Battle.SUMMON_MENU

			# BATTLE MENU
			elif self.game.state == 1 and self.battle.state == Battle.FIGHT_MENU:
				if Input().key_up(key_code= Input().Y): 
					self.on_screen_text = "Move Y utilizado!"
					self.battle.state = Battle.TEXT_ON_SCREEN
				elif Input().key_up(key_code= Input().A):
					self.on_screen_text = "Move A utilizado!"
					self.battle.state = Battle.TEXT_ON_SCREEN
				elif Input().key_up(key_code= Input().X):
					self.on_screen_text = "Move X utilizado!"
					self.battle.state = Battle.TEXT_ON_SCREEN
				elif Input().key_up(key_code= Input().B):
					self.on_screen_text = "Move B utilizado!"
					self.battle.state = Battle.TEXT_ON_SCREEN
					
			# TEXT ON SCREEN
			elif self.game.state == 1 and self.battle.state == Battle.TEXT_ON_SCREEN:
				if Input().key_up(key_code= Input().A):
					self.on_screen_text = ''
					self.battle.state = Battle.MAIN_MENU
			
			# SUMMON MENU
			elif self.game.state == 1 and self.battle.state == Battle.SUMMON_MENU:
				if Input().key_up(key_code= Input().A):
					if len(self.battle.battleListA) > 0 and self.battle.battleListA[0].currentHP > 0 and self.battle.currentDaoA != self.battle.battleListA[0]:
						self.battle.Summon(Battle.YOU, 0)
						self.on_screen_text = self.battle.currentDaoA.summon_text
						self.battle.state = Battle.TEXT_ON_SCREEN

				elif Input().key_up(key_code= Input().B):
					if len(self.battle.battleListA) > 1 and self.battle.battleListA[1].currentHP > 1 and self.battle.currentDaoA != self.battle.battleListA[1]:
						self.battle.Summon(Battle.YOU, 1)
						self.on_screen_text = self.battle.currentDaoA.summon_text
						self.battle.state = Battle.TEXT_ON_SCREEN

				elif Input().key_up(key_code= Input().X):
					if len(self.battle.battleListA) > 2 and self.battle.battleListA[2].currentHP > 2 and self.battle.currentDaoA != self.battle.battleListA[2]:
						self.battle.Summon(Battle.YOU, 2)
						self.on_screen_text = self.battle.currentDaoA.summon_text
						self.battle.state = Battle.TEXT_ON_SCREEN

				elif Input().key_up(key_code= Input().Y):
					if len(self.battle.battleListA) > 3 and self.battle.battleListA[3].currentHP > 3 and self.battle.currentDaoA != self.battle.battleListA[3]:
						self.battle.Summon(Battle.YOU, 3)
						self.on_screen_text = self.battle.currentDaoA.summon_text
						self.battle.state = Battle.TEXT_ON_SCREEN

				elif Input().key_up(key_code= Input().L):
					if len(self.battle.battleListA) > 4 and self.battle.battleListA[4].currentHP > 4 and self.battle.currentDaoA != self.battle.battleListA[4]:
						self.battle.Summon(Battle.YOU, 4)
						self.on_screen_text = self.battle.currentDaoA.summon_text
						self.battle.state = Battle.TEXT_ON_SCREEN

				elif Input().key_up(key_code= Input().R):
					if len(self.battle.battleListA) > 5 and self.battle.battleListA[5].currentHP > 5 and self.battle.currentDaoA != self.battle.battleListA[5]:
						self.battle.Summon(Battle.YOU, 5)
						self.on_screen_text = self.battle.currentDaoA.summon_text
						self.battle.state = Battle.TEXT_ON_SCREEN

		### PROVISÓRIO ###
			if Input().key_down(key_code= Input().start):
				self.battle.currentDaoA.set_sprits()
				self.battle.currentDaoB.set_sprits()
				self.battle.currentDaoA.on_screen = True
				self.battle.currentDaoB.on_screen = True

		if self.game.state == 0 and Input().key_down(key_code= Input().select):
			daoA1: Dao = self.daos['6']
			daoA2 = self.daos['106']
			daoA3 = self.daos['215']
			daoA4 = self.daos['122']
			daoA5 = self.daos['200']
			
			daoA1.level = 5
			daoA2.level = 10
			daoA3.level = 3
			daoA4.level = 8
			daoA5.level = 2

			daoA1.summon_text = f"Nascido do fogo e da forja, eu clamo por seu poder, surja! {daoA1.name}!"
			daoA2.summon_text = f"Sua força é inigualável, invoco o seu espirito! venha {daoA2.name}!"

			daoA1.moves.append(self.moves["1"])
			daoA1.moves.append(self.moves["10"])
			daoA1.moves.append(self.moves["52"])

			self.game.player.Insert_dao(daoA1)
			self.game.player.Insert_dao(daoA2)
			self.game.player.Insert_dao(daoA3)
			self.game.player.Insert_dao(daoA4)
			self.game.player.Insert_dao(daoA5)

			daoB1 = self.daos['6']
			daoB2 = self.daos['20']
			daoB3 = self.daos['30']
			enemy = Guider("Enemy", 0, {}, [daoB1, daoB2, daoB3])

			self.battle.Start(self.game.player, enemy)

		elif self.game.state == 1 and Input().key_down(key_code= Input().select):
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

	def show_button(self, text, textcolor, rect: Rect, l_radius, r_radius, type1= '', type2= ''):
		# draw bg 
		pygame.draw.rect(self.display_surface, UI_BG_COLOR, rect, 
				   border_top_left_radius= l_radius, 
				   border_bottom_left_radius= l_radius,
				   border_top_right_radius= r_radius,
				   border_bottom_right_radius= r_radius)
		
		# draw type bg (if needs)
		if type1 != '':
			line_width = BUTTON_HEIGTH // 10

			rect_L = pygame.Rect(rect.x, rect.y, BUTTON_WIDTH // 2 , BUTTON_HEIGTH)
			rect_R = pygame.Rect(rect.centerx, rect.y, BUTTON_WIDTH // 2, BUTTON_HEIGTH)
			rect_culling = pygame.Rect(rect.centerx - BUTTON_HEIGTH // 2, rect.centery - (BUTTON_HEIGTH - 2 * line_width) // 2, BUTTON_HEIGTH, BUTTON_HEIGTH - 2 * line_width)

			pygame.draw.rect(self.display_surface,
				self.colorChart[type1], 
				rect_L,
				border_top_left_radius= l_radius, 
				border_bottom_left_radius= l_radius,
				width= line_width)
		
			pygame.draw.rect(self.display_surface, 
				self.colorChart[type2] if type2 != '' else self.colorChart[type1], 
				rect_R,
				border_top_right_radius= r_radius,
				border_bottom_right_radius= r_radius,
				width= line_width)
			
			pygame.draw.rect(self.display_surface, UI_BG_COLOR, rect_culling)
		
		# Text offset
		text_surface = self.font_medium.render(text, True, textcolor)

		padding_X = text_surface.get_rect().width // 2
		padding_Y = text_surface.get_rect().height // 2
		
		text_rect = pygame.Rect((rect.centerx - padding_X), (rect.centery - padding_Y), BUTTON_WIDTH, BUTTON_HEIGTH)

		# draw text
		self.display_surface.blit(text_surface, text_rect)

	def show_button_UI(self, text, button_ID, color, active_color, pos_X, pos_Y, l_radius, r_radius):
		rect = pygame.Rect(pos_X, pos_Y, BUTTON_HEIGTH, BUTTON_HEIGTH)
		
		# Draw bg
		selected_color = active_color if Input().key_hold(button_ID) else color

		pygame.draw.rect(self.display_surface, selected_color, rect,
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
	
	def show_type_icon(self, type, pos_X, pos_Y):
		rect = pygame.Rect(pos_X, pos_Y, TYPE_ICON_WIDTH, TYPE_ICON_HEIGTH)

		# Draw bg
		pygame.draw.rect(self.display_surface, self.colorChart[type], rect, border_radius=(TYPE_ICON_HEIGTH // 2))

		# Contorno
		# pygame.draw.rect(self.display_surface, TEXT_COLOR, rect, border_radius=(TYPE_ICON_HEIGTH // 2), width= TYPE_ICON_HEIGTH // 10)
		
		# Text offset
		self.font_type.set_bold(True)
		text_surface = self.font_type.render(type, True, TEXT_COLOR)

		padding_X = text_surface.get_rect().width // 2
		padding_Y = text_surface.get_rect().height // 2
		
		text_rect = pygame.Rect((rect.centerx - padding_X), (rect.centery - padding_Y), TYPE_ICON_WIDTH, TYPE_ICON_HEIGTH)

		# draw text
		self.display_surface.blit(text_surface, text_rect)

	def show_chatbox(self, textcolor):
		# draw bg and button
		rect = pygame.Rect(CHATBOX_POS_X, CHATBOX_POS_Y, CHATBOX_WIDTH, CHATBOX_HEIGTH)
		pygame.draw.rect(self.display_surface, UI_BG_COLOR, rect, border_radius= int(HALF_UNIT))
		self.show_button_UI("A", Input().A, ABXY_COLOR, ON_SELECT_COLOR, CHATBOX_BUTTON_X, CHATBOX_BUTTON_Y, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)

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
		self.show_text(f"{int(self.battle.currentDaoA.currentHP)} / {int(self.battle.currentDaoA.HP)}" if self.battle.currentDaoA.currentHP > 0 else "Defeated", self.daoA_hptext, TEXT_COLOR)
		self.show_text(f"{self.battle.currentDaoA.name} {"◊" * self.battle.currentDaoA.level}", self.daoA_name, TEXT_COLOR)
		self.show_text(f"+{self.battle.initA}", self.daoA_init, TEXT_COLOR)
		self.show_type_icon(self.battle.currentDaoA.type1, TYPE_ICON1_A_POS_X, TYPE_ICON1_A_POS_Y)
		if self.battle.currentDaoA.type2 != "":
			self.show_type_icon(self.battle.currentDaoA.type2, TYPE_ICON2_A_POS_X, TYPE_ICON2_A_POS_Y)

		self.daoB_hpsize = self.daoB_hpsize + (self.battle.currentDaoB.currentHP - self.daoB_hpsize) * (0.05)
		self.show_bar(int(self.battle.currentDaoB.currentHP), int(self.battle.currentDaoB.HP), self.daoB_hpsize, self.daoB_hpbar, HP_COLOR, HP_SHADOW_COLOR)
		self.show_text(f"{int(self.battle.currentDaoB.currentHP)} / {int(self.battle.currentDaoB.HP)}" if self.battle.currentDaoB.currentHP > 0 else "Defeated", self.daoB_hptext, TEXT_COLOR)
		self.show_text(f"{self.battle.currentDaoB.name} {"◊" * self.battle.currentDaoB.level}", self.daoB_name, TEXT_COLOR)
		self.show_text(f"+{self.battle.initB}", self.daoB_init, TEXT_COLOR)
		self.show_type_icon(self.battle.currentDaoB.type1, TYPE_ICON1_B_POS_X, TYPE_ICON1_B_POS_Y)
		if self.battle.currentDaoB.type2 != "":
			self.show_type_icon(self.battle.currentDaoB.type2, TYPE_ICON2_B_POS_X, TYPE_ICON2_B_POS_Y)

		# Daos sprites
		self.battle.currentDaoA.show_dao(self.display_surface, DAO_A_POS_X, DAO_A_POS_Y, side="B")
		self.battle.currentDaoB.show_dao(self.display_surface, DAO_B_POS_X, DAO_B_POS_Y, side="A")

		# Situacional UI
		if self.battle.state == Battle.MAIN_MENU:
			self.show_button_UI("B", Input().B, ABXY_COLOR, ON_SELECT_COLOR, BUTTON_B_X, BUTTON_B_Y, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)
			self.show_button("Summon", TEXT_COLOR, self.button_rect_B, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)

			self.show_button_UI("X", Input().X, ABXY_COLOR, ON_SELECT_COLOR, BUTTON_X_X, BUTTON_X_Y, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)
			self.show_button("Fight", TEXT_COLOR, self.button_rect_X, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)

			# self.show_button_UI("A", Input().A, ABXY_COLOR, ON_SELECT_COLOR, BUTTON_A_X, BUTTON_A_Y, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)
			# self.show_button("Give up", RED_TEXT_COLOR, self.button_rect_A, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)

		elif self.battle.state == Battle.FIGHT_MENU:
			self.show_button_UI("Y", Input().Y, ABXY_COLOR, ON_SELECT_COLOR, BUTTON_Y_X, BUTTON_Y_Y, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)
			moveY = self.battle.currentDaoA.moves[0].name if 0 < len(self.battle.currentDaoA.moves) else ""
			self.show_button(moveY, TEXT_COLOR, self.button_rect_Y, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS, type1= self.battle.currentDaoA.moves[0].type if len(self.battle.currentDaoA.moves) > 0 else "")

			self.show_button_UI("X", Input().X, ABXY_COLOR, ON_SELECT_COLOR, BUTTON_X_X, BUTTON_X_Y, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)
			moveX = self.battle.currentDaoA.moves[1].name if 1 < len(self.battle.currentDaoA.moves) else ""
			self.show_button(moveX, TEXT_COLOR, self.button_rect_X, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS, type1= self.battle.currentDaoA.moves[1].type if len(self.battle.currentDaoA.moves) > 1 else "")

			self.show_button_UI("B", Input().B, ABXY_COLOR, ON_SELECT_COLOR, BUTTON_B_X, BUTTON_B_Y, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)
			moveB = self.battle.currentDaoA.moves[2].name if 2 < len(self.battle.currentDaoA.moves) else ""
			self.show_button(moveB, TEXT_COLOR, self.button_rect_B, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS, type1= self.battle.currentDaoA.moves[2].type if len(self.battle.currentDaoA.moves) > 2 else "")

			self.show_button_UI("A", Input().A, ABXY_COLOR, ON_SELECT_COLOR, BUTTON_A_X, BUTTON_A_Y, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)
			moveA = self.battle.currentDaoA.moves[3].name if 3 < len(self.battle.currentDaoA.moves) else ""
			self.show_button(moveA, TEXT_COLOR, self.button_rect_A, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS, type1= self.battle.currentDaoA.moves[3].type if len(self.battle.currentDaoA.moves) > 3 else "")

		elif self.battle.state == Battle.SUMMON_MENU:
			# Button A
			dao_A_type1 = self.battle.battleListA[0].type1 if len(self.battle.battleListA) > 0 else ""
			dao_A_type2 = self.battle.battleListA[0].type2 if len(self.battle.battleListA) > 0 else ""
			dao_A = f"◊ {self.battle.battleListA[0].level}x {self.battle.battleListA[0].name}" if len(self.battle.battleListA) > 0 else ""
			self.show_button(dao_A, TEXT_COLOR if (len(self.battle.battleListA) > 0 and self.battle.battleListA[0].currentHP > 0) else RED_TEXT_COLOR, self.button_rect_A, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS, type1= dao_A_type1, type2= dao_A_type2)
			self.show_button_UI("A", Input().A, ABXY_COLOR, ON_SELECT_COLOR, BUTTON_A_X, BUTTON_A_Y, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)

			# Button B
			dao_B_type1 = self.battle.battleListA[1].type1 if len(self.battle.battleListA) > 1 else ""
			dao_B_type2 = self.battle.battleListA[1].type2 if len(self.battle.battleListA) > 1 else ""
			dao_B = f"◊ {self.battle.battleListA[1].level}x {self.battle.battleListA[1].name}" if len(self.battle.battleListA) > 1 else ""
			self.show_button(dao_B, TEXT_COLOR if (len(self.battle.battleListA) > 1 and self.battle.battleListA[1].currentHP > 0) else RED_TEXT_COLOR, self.button_rect_B, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS, type1= dao_B_type1, type2= dao_B_type2)
			self.show_button_UI("B", Input().B, ABXY_COLOR, ON_SELECT_COLOR, BUTTON_B_X, BUTTON_B_Y, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)

			# Button X
			dao_X_type1 = self.battle.battleListA[2].type1 if len(self.battle.battleListA) > 2 else ""
			dao_X_type2 = self.battle.battleListA[2].type2 if len(self.battle.battleListA) > 2 else ""
			dao_X = f"◊ {self.battle.battleListA[2].level}x {self.battle.battleListA[2].name}" if len(self.battle.battleListA) > 2 else ""
			self.show_button(dao_X, TEXT_COLOR if (len(self.battle.battleListA) > 2 and self.battle.battleListA[2].currentHP > 0) else RED_TEXT_COLOR, self.button_rect_X, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS, type1= dao_X_type1, type2= dao_X_type2)
			self.show_button_UI("X", Input().X, ABXY_COLOR, ON_SELECT_COLOR, BUTTON_X_X, BUTTON_X_Y, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)

			# Button Y
			dao_Y_type1 = self.battle.battleListA[3].type1 if len(self.battle.battleListA) > 3 else ""
			dao_Y_type2 = self.battle.battleListA[3].type2 if len(self.battle.battleListA) > 3 else ""
			dao_Y = f"◊ {self.battle.battleListA[3].level}x {self.battle.battleListA[3].name}" if len(self.battle.battleListA) > 3 else ""
			self.show_button(dao_Y, TEXT_COLOR if (len(self.battle.battleListA) > 3 and self.battle.battleListA[3].currentHP > 0) else RED_TEXT_COLOR, self.button_rect_Y, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS, type1= dao_Y_type1, type2= dao_Y_type2)
			self.show_button_UI("Y", Input().Y, ABXY_COLOR, ON_SELECT_COLOR, BUTTON_Y_X, BUTTON_Y_Y, BUTTON_ABXY_RADIUS, BUTTON_ABXY_RADIUS)

			# Button L
			dao_L_type1 = self.battle.battleListA[4].type1 if len(self.battle.battleListA) > 4 else ""
			dao_L_type2 = self.battle.battleListA[4].type2 if len(self.battle.battleListA) > 4 else ""
			dao_L = f"◊ {self.battle.battleListA[4].level}x {self.battle.battleListA[4].name}" if len(self.battle.battleListA) > 4 else ""
			self.show_button(dao_L, TEXT_COLOR if (len(self.battle.battleListA) > 4 and self.battle.battleListA[4].currentHP > 0) else RED_TEXT_COLOR, self.button_rect_L, BUTTON_ABXY_RADIUS, 0, type1= dao_L_type1, type2= dao_L_type2)
			self.show_button_UI("L", Input().L, ABXY_COLOR, ON_SELECT_COLOR, BUTTON_L_X, BUTTON_L_Y, 0, BUTTON_ABXY_RADIUS)

			# Button R
			dao_R_type1 = self.battle.battleListA[5].type1 if len(self.battle.battleListA) > 5 else ""
			dao_R_type2 = self.battle.battleListA[5].type2 if len(self.battle.battleListA) > 5 else ""
			dao_R = f"◊ {self.battle.battleListA[5].level}x {self.battle.battleListA[5].name}" if len(self.battle.battleListA) > 5 else ""
			self.show_button(dao_R, TEXT_COLOR if (len(self.battle.battleListA) > 5 and self.battle.battleListA[5].currentHP > 0) else RED_TEXT_COLOR, self.button_rect_R, 0, BUTTON_ABXY_RADIUS, type1= dao_R_type1, type2= dao_R_type2)
			self.show_button_UI("R", Input().R, ABXY_COLOR, ON_SELECT_COLOR, BUTTON_R_X, BUTTON_R_Y, BUTTON_ABXY_RADIUS, 0)

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
