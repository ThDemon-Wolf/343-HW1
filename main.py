#!/usr/bin/env python3

import pygame as pg
import pygame.freetype
import os
from enemy import Enemy
from player import Player
from projectile import Projectile
from pygame.locals import *

def main():
    # Startup pygame
    pg.init()

    # Get a screen object
    screen = pg.display.set_mode([1024, 768])

    # Create a player - TODO
    player = Player()

    # Create enemy and projectile Groups - TODO
    enemies = pg.sprite.Group()
    projectiles = pg.sprite.Group()

    for i in range(500, 1000, 75):
        for j in range(100, 600, 50):
            enemy = Enemy((i, j))
            enemies.add(enemy)

    # Start sound - Load background music and start it
    # playing on a loop - TODO
    pg.mixer.music.load(os.path.join('assets', 'background_music.wav'))
    pg.mixer.music.play(-1)  # Loop indefinitely

    # Get font setup
    pg.freetype.init()
    font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./assets", "PermanentMarker-Regular.ttf")
    font_size = 64
    font = pg.freetype.Font(font_path, font_size)
    # Make a tuple for FONTCOLOR - TODO
    FONTCOLOR = (255, 255, 255)  # White color

    # Startup the main game loop
    running = True
    # Keep track of time
    delta = 0
    # Make sure we can't fire more than once every 250ms
    shotDelta = 0.25  # Start at the limit to allow immediate firing
    # Frame limiting
    fps = 60
    clock = pg.time.Clock()
    clock.tick(fps)
    # Setup score variable
    score = 0
    while running:

        # First thing we need to clear the events.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.USEREVENT + 1:
                score += 100

        keys = pg.key.get_pressed()

        if keys[K_s] or keys[K_DOWN]:
            player.down(delta)
        if keys[K_w] or keys[K_UP]:
            player.up(delta)
        if keys[K_SPACE]:
            if shotDelta >= 0.25:
                projectile = Projectile(player.rect, enemies)
                projectiles.add(projectile)
                shotDelta = 0
        # Check if all enemies are cleared - TODO
        if len(enemies) == 0:
            # Display a victory message and end the game
            font.render_to(screen, (400, 350), "You Win!", FONTCOLOR, None, size=64)
            pg.display.flip()
            pg.time.wait(2000)
            running = False

        # Ok, events are handled, let's update objects!
        player.update(delta)
        enemies.update(delta)
        projectiles.update(delta)

        # Objects are updated, now let's draw!
        screen.fill((0, 0, 0))
        player.draw(screen)
        enemies.draw(screen)
        projectiles.draw(screen)
        font.render_to(screen, (10, 10), "Score: " + str(score), FONTCOLOR, None, size=32)

        # When drawing is done, flip the buffer.
        pg.display.flip()

        # How much time has passed this loop?
        delta = clock.tick(fps) / 1000.0
        shotDelta += delta

    # Clean up and quit
    pg.quit()

# Startup the main method to get things going.
if __name__ == "__main__":
    main()