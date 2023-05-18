import pygame
from checkers.constants import WIDTH,HEIGHT,SQUARE_SIZE,WHITE,RED
import time
from checkers.board import Board
from checkers.game import Game
from minimax.algorithm import minimax,minimax2

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
    #board = Board()
    game = Game(WIN)

    while run:
       # clock.tick()
        clock.tick(FPS)
        if game.turn == WHITE:
            time.sleep(0.5)
            value, new_board = minimax(game.get_board(), 1 , float('-inf'), float('inf'), WHITE, game)
            game.ai_move(new_board)

        if game.turn == RED:
            time.sleep(0.5)
            value, new_board = minimax2(game.get_board(), 1, RED, game)
            game.ai_move(new_board)
        game.update()
    pygame.quit()

if __name__ == '__main__':
    main()

'''        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
    
        board.draw(WIN)
        pygame.display.update()

    pygame.quit()'''

'''
        if game.winner() != None:
            print(game.winner())
            run = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
 '''   