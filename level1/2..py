def solution(board, moves):
    stack = []
    answer = 0
    pos = [0] * len(board)
    for i in range(len(board)):
        column = [row[i] for row in board]

        while pos[i] == 0:
            if len(column) > 0:
                for j, elt in enumerate(column):
                    if elt > 0:
                        pos[i] = j
                        break
            else:
                break
    # print('pos', pos)

    for move in moves:
        h = pos[move-1]
        # print(move, h)
        if h < len(pos) -1 :
            val = board[h][move-1]
        else:
            val = 0
        # print(val)
        if val > 0:
            stack.append(val)
            pos[move-1] = pos[move-1] + 1
        if len(stack) > 1:
            # print('stack',stack[-1], stack[-2])
            if stack[-1] == stack[-2]:
                stack = stack[:-2]

    answer = len(stack)
    return answer


def solution2(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                print(i,j, stacklist)
                break

    return answer


if __name__=='__main__':
    # arr = range(2, 100, 2)
    # print(arr)
    # bin = binary_search(arr, 30)
    # print(bin)

    board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
    moves = [1,5,3,5,1,2,1,4]
    # print(board[1][2])
    sol = solution2(board, moves)
    print(sol)