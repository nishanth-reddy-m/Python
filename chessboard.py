def ranks():
    rank = []
    for i in range(8,0,-1):
        n = [str(i) for j in range(1,9)]
        rank.append(n)
    return rank

def files():
    file = [[chr(i) for i in range(65,73)] for i in range(8)]
    return file

row = ranks()
column = files()
board = []
for i in range(len(row)):
    boardc=[column[i][j]+row[i][j] for j in range(len(column[i]))]
    board.append(boardc)
for i in board:
    print(i)