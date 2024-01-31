import pygame, sys, os
from settings import *
from debug import *
from ui import *
from utils import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Dao's Guide")

        self.battleUI = BattleUI()

    def run(self):
        # Test        
        daoA1 = getDao(archiveName= os.path.join("Data", "Daos.csv"), ID= '3')
        daoA2 = getDao(archiveName= os.path.join("Data", "Daos.csv"), ID= '10')
        daoA3 = getDao(archiveName= os.path.join("Data", "Daos.csv"), ID= '20')

        daoB1 = getDao(archiveName= os.path.join("Data", "Daos.csv"), ID= '6')
        daoB2 = getDao(archiveName= os.path.join("Data", "Daos.csv"), ID= '15')
        daoB3 = getDao(archiveName= os.path.join("Data", "Daos.csv"), ID= '25')

        battle = Battle([daoA1, daoA2, daoA3], [daoB1, daoB2, daoB3])
        battle.Start()


        while True: 
            for event in pygame.event.get():
                # Filtro evento de fechar o jogo
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Filtro evento de input
                elif event.type == pygame.KEYDOWN:
                    pass
            
            # Showing area
            self.screen.fill('#728a72')
            self.battleUI.display(battle)

            # Debug area
            debug("")
            battle.currentDaoA.currentHP -= 10 * (self.clock.tick(FPS) / 1000)

            if battle.currentDaoA.currentHP <= 0:
                battle.Summon(Battle.YOU, 2)

            # Update screen
            pygame.display.update()
            self.clock.tick(FPS)

game = Game()
game.run()