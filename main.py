import pygame
from checkers.constants import WIDTH,HEIGHT,SQUARE_SIZE
from checkers.board import Board
from checkers.game import Game

FPS = 60.0

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Checkers!!')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    game = Game(WIN)

    while run:
       # clock.tick()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
    
        board.draw(WIN)
        pygame.display.update()
    pygame.quit()
       