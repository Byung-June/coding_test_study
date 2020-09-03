# 10:04
def rot(mat):
    return [i for i in zip(*mat[::-1])]


def pos(mat, val):
    position = []
    if val == 'key':
        k = 1
    else:
        k = 0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == k:
                position.append([i,j])

    return position

def move_to(mat, k, pos):
    dis = [pos[0] - mat[k][0], pos[1] - mat[k][1]]
    return [[elt[0] + dis[0], elt[1] + dis[1]] for elt in mat]


def solution(key, lock):
    answer = False
    k_pos = pos(key, 'key')
    l_pos = pos(lock, 'lock')
    if len(k_pos) >= len(l_pos):
        rot_num = 0
        while rot_num < 4:
            k_pos = pos(key, 'key')
            for k in range(len(k_pos)):
                # print(rot_num, k_pos, k, l_pos)
                # print('moveto', move_to(k_pos, k, l_pos[0]))
                if all(l in move_to(k_pos, k, l_pos[0]) for l in l_pos):
                    a = [m for m in move_to(k_pos, k, l_pos[0]) if m not in l_pos if m[0] in range(len(key)) if m[1] in range(len(key))]
                    if len(a) == 0:
                        answer = True
                    break
            if answer:
                break
            key = rot(key)
            rot_num += 1

    return answer


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))