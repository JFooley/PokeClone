import pygame, sys
from settings import *
from debug import *
from ui import BattleUI
from battle import Battle
from utils import *

class Game:
    # States
    EXPLORING = 0
    ON_BATTLE = 1
    ON_MENU = 2

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Dao's Guide")


        self.battleObject = Battle()
        self.state: int = 0

    def Update_status(self):
        if self.battleObject.state != Battle.DEFAULT:
            self.state = self.ON_BATTLE
        else:
            self.state = self.EXPLORING

    def run(self):
        battleUI = BattleUI(self.battleObject, self.state)

        while True: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                #     pygame.display.toggle_fullscreen()

            # Must Run
            self.Update_status()
            battleUI.run()

            # Debug

            # Update screen
            pygame.display.update()
            self.clock.tick(FPS)

game = Game()
game.run()