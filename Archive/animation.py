import pygame
import os

class Animation():
    def __init__(self, frames: list, frametime, surface, rectangle):
        self.is_running = False

        self.curret_frame = 0
        self.frames = frames
        self.frametime = frametime

        self.surface = surface
        self.rect = rectangle

        self.last_update = 0

    def Loop(self):
        if not self.is_running:
            self.is_running = True
            self.last_update = pygame.time.get_ticks()

        elif self.is_running:
            current_time = pygame.time.get_ticks()

            if current_time - self.last_update >= self.frametime:
                self.curret_frame += 1
                self.last_update = current_time
                
                if self.curret_frame >= len(self.frames):
                    self.curret_frame = 0

            self.surface.blit(self.frames[self.curret_frame], self.rect)

    def getFrames(name_patern, lenght, folder_path):
        frames = []
        for index in range(lenght):
            frame = pygame.image.load(os.path.join(folder_path, f"{name_patern}{index}.png"))
            frames.append(frame)

        return frames


    