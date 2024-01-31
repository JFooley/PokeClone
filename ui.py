import pygame
from pygame import Rect
from settings import * 
from battle import Battle

class BattleUI:
	# buttons
	BUTTON_MOVE = "BM"
	BUTTON_SIMPLE = "BS"
	BUTTON_DAO = "BD"

	def __init__(self):
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

	def show_bar(self, current, max_amount, bg_rect, color):
		# draw bg 
		pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)

		# converting stat to pixel
		ratio = current / max_amount
		current_width = bg_rect.width * ratio
		current_rect = bg_rect.copy()
		current_rect.width = current_width

		# drawing the bar
		pygame.draw.rect(self.display_surface, color, current_rect)
		# pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)

	def show_text(self, text, rect, color):
		# drawning the text
		text_surface = self.font_medium.render(text, True, color)
		self.display_surface.blit(text_surface, rect)

	def show_button(self, type, text, textcolor, rect: Rect, battle: Battle):
		# draw bg 
		pygame.draw.rect(self.display_surface, UI_BG_COLOR, rect, border_radius= int(BUTTON_HEIGTH // 2))

		# draw text
		if type == self.BUTTON_SIMPLE:
			padding_X = BUTTON_HEIGTH // 2
			padding_Y = 5
			text_offset = pygame.Rect((rect.left + padding_X), (rect.top + padding_Y), BUTTON_WIDTH, BUTTON_HEIGTH)
			text_surface = self.font_medium.render(text, True, textcolor)
			self.display_surface.blit(text_surface, text_offset)

	def show_chatbox(self, text, textcolor, rect: Rect):
		# draw bg
		pygame.draw.rect(self.display_surface, UI_BG_COLOR, rect, border_radius= int(BUTTON_HEIGTH))

		# draw text

	def display(self, battle: Battle):
		# Dao A
		self.show_bar(int(battle.currentDaoA.currentHP), int(battle.currentDaoA.HP), self.daoA_hpbar, HP_COLOR)
		self.show_text(f"{int(battle.currentDaoA.currentHP)} / {int(battle.currentDaoA.HP)}", self.daoA_hptext, TEXT_COLOR)
		self.show_text(f"LV: {battle.currentDaoA.level} {battle.currentDaoA.name}", self.daoA_name, TEXT_COLOR)
		self.show_text(f"+{battle.initA}", self.daoA_init, TEXT_COLOR)

		# Dao B
		self.show_bar(int(battle.currentDaoB.currentHP), int(battle.currentDaoB.HP), self.daoB_hpbar, HP_COLOR)
		self.show_text(f"{int(battle.currentDaoB.currentHP)} / {int(battle.currentDaoB.HP)}", self.daoB_hptext, TEXT_COLOR)
		self.show_text(f"LV: {battle.currentDaoB.level} {battle.currentDaoB.name}", self.daoB_name, TEXT_COLOR)
		self.show_text(f"+{battle.initB}", self.daoB_init, TEXT_COLOR)
		
		if battle.state == Battle.DEFAULT:
			self.show_button(self.BUTTON_SIMPLE, "Summon", TEXT_COLOR, self.fight_menu_right, battle)
			self.show_button(self.BUTTON_SIMPLE, "Fight", TEXT_COLOR, self.fight_menu_left, battle)

		elif battle.state == Battle.FIGHT_MENU:
			self.show_button(self.BUTTON_SIMPLE, "Move A", TEXT_COLOR, self.fight_menu_up, battle)
			self.show_button(self.BUTTON_SIMPLE, "Move B", TEXT_COLOR, self.fight_menu_left, battle)
			self.show_button(self.BUTTON_SIMPLE, "Move C", TEXT_COLOR, self.fight_menu_right, battle)
			self.show_button(self.BUTTON_SIMPLE, "Move D", TEXT_COLOR, self.fight_menu_down, battle)

		elif battle.state == Battle.SUMMON_MENU:
			pass # Colocar as esferas DAO 

		elif battle.state == Battle.TEXT_ON_SCREEN:
			texto_teste = "Ola tudo bem? hahahhaa"
			self.show_chatbox(texto_teste, TEXT_COLOR, self.chat_box)

