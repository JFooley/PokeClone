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

    def initialize(self):
        if not self._initialized:
            self._initialized = True
            self.last_frame = copy.deepcopy(pygame.key.get_pressed())
            self.last_frame_gamepad = None
            self.last_frame_gamepad_hats = None

            if pygame.joystick.get_count() != 0:
                self.input_type = self.GAMEPAD
                joystick = pygame.joystick.Joystick(0)
                joystick.init()

            else:
                self.input_type = self.KEYBOARD

            self.up = None
            self.down = None
            self.left = None
            self.right = None
            self.start = None
            self.select = None
            self.L = None
            self.R = None
            self.A = None
            self.B = None
            self.X = None
            self.Y = None

            self.change_pattern(self.input_type)

        else:
            raise Exception("Input already initialized.")
        
    def update(self):
        if self.input_type == self.KEYBOARD:
            self.last_frame = copy.deepcopy(pygame.key.get_pressed())
        elif self.input_type == self.GAMEPAD:
            self.last_frame_gamepad = [[pygame.joystick.Joystick(0).get_button(i) for i in range(pygame.joystick.Joystick(0).get_numbuttons())]]
            self.last_frame_gamepad_hats = pygame.joystick.Joystick(0).get_hat(0)

    def change_pattern(self, pattern):
        self.input_type = pattern

        if pattern == self.KEYBOARD:
            self.up = pygame.K_UP
            self.down = pygame.K_DOWN
            self.left = pygame.K_LEFT
            self.right = pygame.K_RIGHT
            self.start = pygame.K_SPACE
            self.select = pygame.K_RETURN
            self.L = pygame.K_q
            self.R = pygame.K_e
            self.A = pygame.K_s
            self.B = pygame.K_d
            self.X = pygame.K_a
            self.Y = pygame.K_w

        elif pattern == self.GAMEPAD:
            self.up = "(0, 1)"
            self.down = "(0, -1)"
            self.left = "(-1, 0)"
            self.right = "(1, 0)"
            self.start = 7
            self.select = 6
            self.L = 4
            self.R = 5
            self.A = 0
            self.B = 1
            self.X = 2
            self.Y = 3

    def handle_joystick_events(self, event):
        if event.type == pygame.JOYDEVICEADDED:
            self.change_pattern(self.GAMEPAD)
            joystick = pygame.joystick.Joystick(0)
            joystick.init()
            self.update()

        elif event.type == pygame.JOYDEVICEREMOVED:
            self.change_pattern(self.KEYBOARD)
            self.update()
            
        # You can call this method in the event handler looping to change automatically between
        # keyboard and gamepad when a joystick is coneccted. You can change the class to detect
        # when a especific button is pressed to change the pattern.

        # Self.update() call ensures that self.last_frame will be correct to the current pattern 

    def key_hold(self, key_code):
        if self.input_type == self.GAMEPAD:
            if type(key_code) == str: # When the pressed buton is a hat button
                return (repr(pygame.joystick.Joystick(0).get_hat(0)) == key_code)
            else:
                return pygame.joystick.Joystick(0).get_button(key_code)
        else:
            return pygame.key.get_pressed()[key_code]

    def key_down(self, key_code):
        if self.input_type == self.GAMEPAD:
            if type(key_code) == str: # When the pressed buton is a hat button
                return (repr(pygame.joystick.Joystick(0).get_hat(0)) == key_code) and self.last_frame_gamepad_hats != pygame.joystick.Joystick(0).get_hat(0)
            else:
                return pygame.joystick.Joystick(0).get_button(key_code) and not self.last_frame_gamepad[0][key_code]
        else:
            return not self.last_frame[key_code] and pygame.key.get_pressed()[key_code]

    def key_up(self, key_code):
        if self.input_type == self.GAMEPAD:
            if type(key_code) == str: # When the pressed buton is a hat button
                return (repr(pygame.joystick.Joystick(0).get_hat(0)) == key_code) and self.last_frame_gamepad_hats != pygame.joystick.Joystick(0).get_hat(0)
            else:
                return not pygame.joystick.Joystick(0).get_button(key_code) and self.last_frame_gamepad[0][key_code]
        else: 
            return self.last_frame[key_code] and not pygame.key.get_pressed()[key_code]
