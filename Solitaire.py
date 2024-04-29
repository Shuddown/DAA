board = [[8, 6, 2, 3,55],
         [9, 7, 1, 2,54]]

def row_val(board):
    return abs(board[0][0] - board[0][1]) + abs(board[1][0] - board[1][1])

def col_val(board):
    return abs(board[0][0] - board[1][0])

def best_pairs(board):
    if len(board[0]) == 0: return 0
    if len(board[0]) == 1: return col_val(board)
    return max(row_val(board) + best_pairs([board[0][2:], board[1][2:]]), col_val(board) + best_pairs([board[0][1:], board[1][1:]]))


print(best_pairs(board))
            