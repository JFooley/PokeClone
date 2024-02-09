import pygame
import copy

##### OBSERVAÇÕES PARA O USO CORRETO DA CLASSE #####
# Essa é uma classe singleton, ou seja, só possui uma instancia do objeto.
# Ela é feita dessa forma para poder ser acessada de forma igual em qualquer parte do código
# independente da cena que esteja sendo rodada. Ela só existe pois o pygame naturalmente não
# possui um método de verificação de Key Up e Key Down, então precisa fazer gambiarra.
# Para usar corretamente, no ínicio do código ela precisa ser instanciada e chamar o método initialize().
# Dai em diante basta importar e chamar Input() (com o parêntese, já que queremos o objeto) e usar seus métodos

class Input:
    KEYBOARD = 1
    GAMEPAD = 2

    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance

    def initialize(self, pattern):
        if not self._initialized:
            self.last_frame = copy.deepcopy(pygame.key.get_pressed())

            if pattern == self.KEYBOARD:
                self.up = pygame.K_UP
                self.down = pygame.K_DOWN
                self.left = pygame.K_LEFT
                self.right = pygame.K_RIGHT
                self.start = pygame.K_SPACE
                self.select = pygame.K_m
                self.A = pygame.K_s
                self.B = pygame.K_d
                self.X = pygame.K_a
                self.Y = pygame.K_w

            elif pattern == self.GAMEPAD:
                self.up = 11
                self.down = 12
                self.left = 13
                self.right = 14
                self.start = 8
                self.select = 7
                self.A = 1
                self.B = 2
                self.X = 3
                self.Y = 4

            self._initialized = True
        else:
            raise Exception("Input already initialized.")

    def set_keys(self, up, down, left, right, start, select, A, B, X, Y):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.start = start
        self.select = select
        self.A = A
        self.B = B
        self.X = Y
        self.Y = Y

    def update(self):
        self.last_frame = copy.deepcopy(pygame.key.get_pressed())

    def key_hold(self, key_code):
        return pygame.key.get_pressed()[key_code]

    def key_down(self, key_code):
        if not self.last_frame[key_code] and pygame.key.get_pressed()[key_code]:
            return True
        else:
            return False

    def key_up(self, key_code):
        if self.last_frame[key_code] and not pygame.key.get_pressed()[key_code]:
            return True
        else:
            return False