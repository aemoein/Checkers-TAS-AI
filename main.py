import pygame
from checkers.constants import WIDTH,HEIGHT,SQUARE_SIZE
FPS = 60.0

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Checkers!!')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col
