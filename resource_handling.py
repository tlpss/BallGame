import os
import pygame

class Loader:

    @staticmethod
    def load_png(name):
        dir_name = 'data'
        fullname = os.path.join(dir_name,name)
        image = pygame.image.load(fullname)
        image = image.convert()
        return image
