def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    for indexX in range(0,len(board)):
        for indexY in range(0,len(board[0])):
            if board[indexX][indexY] == word[0]:
                result = backtrack(board, word[1:], indexX, indexY, {})
                if result:
                    return True
    return False


def backtrack(board, word, x, y, dicMap):
    if x + 1 >= len(board):
        pass
    elif board[x+1][y] == word[0] and (str(x+1)+str(y)) not in dicMap:
        if len(word) == 1:
            return True
        else:
            dictCopy = dict(dicMap)
            dictCopy[str(x+1) + str(y)] = 1
            result = backtrack(board, word[1:], x+1, y, dictCopy)
            if result:
                return True
    if x - 1 < 0:
        pass
    elif board[x-1][y] == word[0] and (str(x-1)+str(y)) not in dicMap:
        if len(word) == 1:
            return True
        else:
            dictCopy = dict(dicMap)
            dictCopy[str(x-1) + str(y)] = 1
            result = backtrack(board, word[1:], x-1, y, dictCopy)
            if result:
                return True

    if y + 1 >= len(board[0]):
        pass
    elif board[x][y+1] == word[0] and (str(x)+str(y+1)) not in dicMap:
        if len(word) == 1:
            return True
        else:
            dictCopy = dict(dicMap)
            dictCopy[str(x) + str(y+1)] = 1
            result = backtrack(board, word[1:], x, y+1, dictCopy)
            if result:
                return True

    if y - 1 < 0:
        pass
    elif board[x][y-1] == word[0] and (str(x)+str(y-1)) not in dicMap:
        if len(word) == 1:
            return True
        else:
            dictCopy = dict(dicMap)
            dictCopy[str(x) + str(y-1)] = 1
            result = backtrack(board, word[1:], x, y-1, dictCopy)
            if result:
                return True
    return False


print(exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']],'ABCCED'))

