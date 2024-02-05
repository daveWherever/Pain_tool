import pygame as pg

class Canvas():
    def __init__(self, image):
        self.image = image
        self.image.fill("green")

    def draw(self, surface):
        surface.blit(self.image, (0, 0))