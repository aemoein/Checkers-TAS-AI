from copy import deepcopy
import pygame

RED = (255, 56, 71)
WHITE = (255, 255, 255)

def minimax(position, depth, alpha, beta, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth-1,alpha, beta,False, game)[0]
            maxEval = max(maxEval, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
            if maxEval == evaluation:
                best_move = move
        
        return maxEval, best_move

    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED,game):
            evaluation = minimax(move, depth-1,alpha, beta,True,game)[0]
            minEval = min(minEval,evaluation)
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
            if minEval == evaluation:
                best_move = move
        
        return minEval,best_move




def minimax2(position, depth, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax2(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        
        return maxEval, best_move

    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, WHITE,game):
            evaluation = minimax2(move, depth-1,True,game)[0]
            minEval = min(minEval,evaluation)
            if minEval == evaluation:
                best_move = move
        
        return minEval,best_move




def simulate_move(piece, move, board, game,skip):
    board.move(piece,move[0],move[1])
    if skip:
        board.remove(skip)
    
    return board

def get_all_moves(board,color,game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_move = board.get_valid_moves(piece)
        for move, skip in valid_move.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game,skip)
            moves.append(new_board)
    
    return moves