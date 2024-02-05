import pygame as pg
import constants as c

class Tool(pg.sprite.Sprite):
    def __init__(self, image, pos, size):
        super().__init__()
        self.image = image
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.size = size

    def movement(self):
        pg.mouse.set_visible(False)
        mouse_pos = pg.mouse.get_pos()
        self.rect.center = mouse_pos
        if mouse_pos[0] > c.WINDOW_WIDTH - self.size/2:
            pg.mouse.set_visible(True)

    def window_threshold(self):
        if self.rect.x > c.WINDOW_WIDTH - self.size:
            self.rect.x = c.WINDOW_WIDTH - self.size
        elif self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.y > c.WINDOW_HEIGHT - self.size:
            self.rect.y = c.WINDOW_HEIGHT - self.size
        elif self.rect.y < 0:
            self.rect.y = 0

    def update_size(self, new_image, new_size):
        self.image = new_image
        self.size = new_size
        self.rect = self.image.get_rect(topleft=self.rect.topleft)

    def update(self, screen):
        self.movement()
        self.window_threshold()