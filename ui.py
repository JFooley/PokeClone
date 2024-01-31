import pygame
from settings import * 
from battle import Battle

class BattleUI:
	def __init__(self):
		# general 
		self.display_surface = pygame.display.get_surface()
		self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)

		# hp bar setup 
		self.daoA_hpbar = pygame.Rect(HP_A_POS_X, HP_A_POS_Y, HP_BAR_WIDTH, BAR_HEIGHT)
		self.daoB_hpbar = pygame.Rect(HP_B_POS_X, HP_B_POS_Y, HP_BAR_WIDTH, BAR_HEIGHT)
		self.daoA_hptext = pygame.Rect(HPTEXT_A_POS_X, HPTEXT_A_POS_Y, HP_BAR_WIDTH, BAR_HEIGHT)
		self.daoB_hptext = pygame.Rect(HPTEXT_B_POS_X, HPTEXT_B_POS_Y, HP_BAR_WIDTH, BAR_HEIGHT)

		# info text setup
		self.daoA_name = pygame.Rect(NAMETEXT_A_POS_X, NAMETEXT_A_POS_Y, HP_BAR_WIDTH, BAR_HEIGHT)
		self.daoB_name = pygame.Rect(NAMETEXT_B_POS_X, NAMETEXT_B_POS_Y, HP_BAR_WIDTH, BAR_HEIGHT)

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
		text_surface = self.font.render(text, True, color)
		self.display_surface.blit(text_surface, rect)

	def display(self, battle: Battle):
		# Dao A
		self.show_bar(int(battle.currentDaoA.currentHP), int(battle.currentDaoA.HP), self.daoA_hpbar, HP_COLOR)
		self.show_text(f"{int(battle.currentDaoA.currentHP)} / {int(battle.currentDaoA.HP)}", self.daoA_hptext, TEXT_COLOR)
		self.show_text(f"LV: {battle.currentDaoA.level} {battle.currentDaoA.name}", self.daoA_name, TEXT_COLOR)

		# Dao B
		self.show_bar(int(battle.currentDaoB.currentHP), int(battle.currentDaoB.HP), self.daoB_hpbar, HP_COLOR)
		self.show_text(f"{int(battle.currentDaoB.currentHP)} / {int(battle.currentDaoB.HP)}", self.daoB_hptext, TEXT_COLOR)
		self.show_text(f"LV: {battle.currentDaoB.level} {battle.currentDaoB.name}", self.daoB_name, TEXT_COLOR)
