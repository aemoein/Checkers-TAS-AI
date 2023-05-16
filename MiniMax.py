def minimax(position, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or game_over(position)
        return static_evaluation(position)

    if maximizingPlayer:
        maxEval = -float('inf')
        for child in get_children(position):
            eval = minimax(child, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval

    else:
        minEval = float('inf')
        for child in get_children(position):
            eval = minimax(child, depth - 1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval




###############################################################################

currentPosition = [['b','-','b','-','b','-','b','-'],
                  ['-','b','-','b','-','b','-','b'],
                  ['b','-','b','-','b','-','b','-'],
                  ['-','-','-','-','-','-','-','-'],
                  ['-','-','-','-','-','-','-','-'],
                  ['-','w','-','w','-','w','-','w'],
                  ['w','-','w','-','w','-','w','-'],
                  ['-','w','-','w','-','w','-','w']]

minimax(currentPosition, 3, -float('inf'), float('inf'), True)
