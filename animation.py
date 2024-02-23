from settings import FPS
import pygame, os, re

class Animation:
    def __init__(self, fps, name= ""):
        self.name = name
        self.fps = fps

        self.is_playing = False
        self.on_screen = True

        self.sprites = []
        self.current_frame = 0

    def find_images_paths(self, path, name):
        caminhos_imagens = []

        # Check if path exist, create if doesn't
        if not os.path.exists(path):
            os.makedirs(path)
        
        # List archives in path
        arquivos = os.listdir(path)
        
        for arquivo in arquivos:
            # Check if the name contains the pattern
            if re.match(rf"{name}-\d+\.png$", arquivo):
                caminho_completo = os.path.join(path, arquivo)
                caminhos_imagens.append(caminho_completo)
        
        # Sort based on image number
        caminhos_imagens.sort(key=lambda x: int(re.search(rf"{name}-(\d+)\.png$", x).group(1)))
        
        return caminhos_imagens
    
    def set_images(self, base_path, name_pattern):
        paths = self.find_images_paths(base_path, name_pattern)

        # Set a image for every image path
        for path in paths:
            sprite = pygame.image.load(path)
            self.sprites.append(sprite)
    
    def play(self, surface, pos_X, pos_Y, mirrored= False, size= None):
        self.is_playing = True

        if self.on_screen and self.sprites:
            sprite = self.sprites[self.current_frame]
            width, heigth = sprite.get_size()

            # Scaling
            width = width if size == None else int((width * size) / heigth)
            heigth = heigth if size == None else size
            sprite = pygame.transform.scale(sprite, (width, heigth))

            # Mirroring
            if mirrored:
                sprite = pygame.transform.flip(sprite, True, False)
            
            # Show on screen
            surface.blit(sprite, (pos_X - (width // 2), pos_Y - (heigth // 2)))

            # Update frame
            frame_exato = int((pygame.time.get_ticks() / 1000) * FPS) % FPS
            animation_tick = frame_exato % (FPS // self.fps) == 0

            if animation_tick:
                self.current_frame = self.current_frame + 1 if (self.current_frame + 1) < len(self.sprites) else 0

    def play_once(self, surface, pos_X, pos_Y, mirrored= False, size= None):
        self.is_playing = True

        if self.on_screen and self.sprites:
            sprite = self.sprites[self.current_frame]
            width, heigth = sprite.get_size()

             # Scaling
            width = width if size == None else int((width * size) / heigth)
            heigth = heigth if size == None else size
            sprite = pygame.transform.scale(sprite, (width, heigth))

            # Mirroring
            if mirrored:
                sprite = pygame.transform.flip(sprite, True, False)
            
            # Show on screen
            surface.blit(sprite, (pos_X - (width // 2), pos_Y - (heigth // 2)))

            # Update frame
            frame_exato = int((pygame.time.get_ticks() / 1000) * FPS) % FPS
            animation_tick = frame_exato % (FPS // self.fps) == 0

            if animation_tick:
                self.current_frame += 1 if (self.current_frame + 1) < len(self.sprites) else 0

            # Change animation state when finished
            if self.current_frame == (len(self.sprites) - 1):
                self.current_frame = 0
                self.is_playing = False

    def reset(self):
        self.current_frame = 0