import os
import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.image.load(os.path.join('assets', 'Ship6.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 50  # Starting X position
        self.rect.y = 384  # Starting Y position (middle of the screen)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
        pass  # No automatic updates needed for the player in this game

    def up(self, delta):
        # Move up
        self.rect.y -= 500 * delta
        if self.rect.top < 0:
            self.rect.top = 0

    def down(self, delta):
        # Move down
        self.rect.y += 500 * delta
        if self.rect.bottom > 768:
            self.rect.bottom = 768