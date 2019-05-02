import pygame

import random

#############################
# HELPERS FOR TEXT RENDERING
#############################

# Initialize the font library.
pygame.font.init()

class Fonts:
    TEXT_FONT     = pygame.font.SysFont('Impact', 30)
    TITLE_FONT    = pygame.font.SysFont('Impact', 100)
    SUBTITLE_FONT = pygame.font.SysFont('Impact', 50)

class Colors:
    WHITE      = (255, 255, 255)
    BLACK      = (  0,   0,   0)
    RED        = (255,   0,   0)
    GREEN      = (  0, 255,   0)
    BLUE       = (  0,   0, 255)
    CYAN       = (  0, 255, 255)
    MAGENTA    = (255,   0, 255)
    YELLOW     = (255, 255,   0)
    LIGHT_GREY = (192, 192, 192)
    GREY       = (128, 128, 128)
    DARK_GREY  = ( 64,  64,  64)

def draw_text_to_screen(screen, text, x, y, color, font):
    render_text = font.render(text, False, color)
    screen.blit(render_text, (x, y))