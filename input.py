import pygame

class input:
    KEYBOARD = 1
    GAMEPAD = 2

    def __init__(self, pattern):
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

        is_pressed = []
        was_pressed = []

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