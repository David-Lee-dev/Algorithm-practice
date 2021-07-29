def solution(board, moves):
    moved = []
    count = 0
    for x in moves:
        for i in range(len(board)): #board's row
            c = x-1    #choosed cul
            if board[i][c] != 0:
                got = board[i][c]
                board[i][c] = 0
                if len(moved) == 0:
                    moved.append(got)
                elif len(moved) > 0 and got != moved[-1]:
                    moved.append(got)
                else:
                    count += 1
                    del moved[-1]
                break
    return count*2