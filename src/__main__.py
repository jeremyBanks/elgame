from glob import glob
import random
import math
import sys
from itertools import count

import pygame
import pygame.image
import pygame.display
import pygame.freetype
import pygame.image
import pygame.mouse
import pygame.time
from pygame import Surface, Rect

from . import sprite_sheet


def x2(sprite):
    return pygame.transform.scale(
        sprite, (sprite.get_rect().width * 2, sprite.get_rect().height * 2)
    )


def main():
    # Initialize pygame, so it can open a window and start listening for input.
    pygame.init()

    # Initialize a clock we'll use to set the framerate.
    clock = pygame.time.Clock()
    fps = 60
    t = 0

    # Set up the window we'll be drawing in
    window = pygame.display.set_mode([256 * 4, 256])
    pygame.display.set_caption("Smells Like Spam")

    # Load our sprite sheet.
    sprites = sprite_sheet.load("assets/sprites")

    # Load the player image we'll be displaying.
    player_image = sprites[
        random.choice(
            [name for name in sprites if ("Ursus" in name or "Horribilis" in name)]
        )
    ]

    # Load the font we'll use for text.
    font = pygame.freetype.SysFont(pygame.freetype.get_default_font(), 32)

    # Loop forever until we set running to False, when the user tries to exit.
    while True:
        t += 1

        # Wait until it's time for the next frame to be drawn.
        clock.tick(fps)

        # Loop over every input or event that has happened since the last frame.
        for event in pygame.event.get():
            print(event)

            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                print("Exiting because the user told us to.")
                return

        # Fill the background
        window.fill((0, 0, 0))

        text, _ = font.render("Boo!", (0, 0, 0))
        text_position = 32, 32
        window.blit(text, text_position)

        # Draw background layers
        for n, sprite in enumerate(
            (
                sprites["Space"],
                sprites["Horizon"],
                x2(sprites["Floor"]),
                sprites["Darkness"],
            )
        ):
            for x in range(
                -((t * (1 + n)) % (sprite.get_rect().width * 2)),
                256 * 6,
                sprite.get_rect().width,
            ):
                r = sprite.get_rect()
                r.center = (x, 128)
                window.blit(sprite, r)

        x = 0
        for sprite in (
            x2(sprites["Ursus 0"]),
            x2(sprites["Ursus 1"]),
            x2(sprites["Ursus 2"]),
            x2(sprites["Ursus 3"]),
            x2(sprites["Horribilis 0"]),
            x2(sprites["Horribilis 1"]),
            x2(sprites["Horribilis 2"]),
            x2(sprites["Horribilis 3"]),
            x2(sprites["Trophy 0"]),
            x2(sprites["Little Magic 0"]),
            x2(sprites["Little Magic 1"]),
            x2(sprites["Little Magic 2"]),
            x2(sprites["Lepus 8 0"]),
            x2(sprites["Lepus 8 1"]),
            x2(sprites["Lepus 8 2"]),
        ):
            r = sprite.get_rect()
            r.midleft = (x, 128)
            window.blit(sprite, r)
            x += r.width + 1

        # Take the new frame we've drawn and display it.
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
