def is9(list):
    if set(list) == set([i for i in range(1, 10)]) and len(list) == 9:
        return True
    return False


def validSolution(board):
    # row valid
    for i in range(9):
        if not is9(board[i]):
            return  False

    # column valid
    for j in range(9):
        if not is9([board[i][j] for i in range(9)]):
            return False

    # block valid
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not is9([board[i+m][j+n] for m in range(3) for n in range(3)]):
                return False
    return True
