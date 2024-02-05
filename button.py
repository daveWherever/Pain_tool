import pygame as pg

class Button():
    def __init__(self, x, y, image, color):
        self.image = image
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        #get mouse position
        pos = pg.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button
        surface.blit(self.image, self.rect)

        return action