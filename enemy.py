import os
import pygame as pg

class Enemy(pg.sprite.Sprite):
    def __init__(self, position):
        super(Enemy, self).__init__()
        self.image = pg.image.load(os.path.join('assets', 'enemy.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

    def update(self, delta):
        self.rect.x -= 100 * delta
        if self.rect.right < 0:
            self.kill()