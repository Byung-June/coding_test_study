def loc_finder(matrix, switch):
    loc = []
    if switch == 'key':
        switch = 1
    elif switch == 'lock':
        switch = 0
    else:
        raise ValueError

    for i, row in enumerate(matrix):
        for j, elt in enumerate(row):
            if elt == switch:
                loc.append([i,j])
    return loc


def check_fit(key_loc, lock_spot, lock_loc, n):
    rotated = 0
    while rotated <= 3:
        for k in key_loc:
            distance = lock_spot[0] - k[0], lock_spot[1] - k[1]
            moved = [[kk[0] + distance[0], kk[1] + distance[1]] for kk in key_loc
                     if (0 <= kk[0] + distance[0] < n) and (0 <= kk[1] + distance[1] < n)]
            # print('!!', lock_spot, 'moved', moved, '!!', lock_loc)
            if all(l in moved for l in lock_loc) and all(l in lock_loc for l in moved):
                return True
        key_loc = rotation(key_loc, n)
        rotated += 1
    return False


def rotation(mat_list, n):
    return [[j, n-1-i]for i, j in mat_list]


def solution(key, lock):
    answer = False

    key_loc = loc_finder(key, 'key')
    lock_loc = loc_finder(lock, 'lock')

    if len(lock_loc) == 0:
        return True

    for lock_spot in lock_loc:
        if check_fit(key_loc, lock_spot, lock_loc, n=len(lock)):
            return True
    return answer



test_key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
test_lock = [[1, 1, 1], [1, 1, 1], [1, 0, 0]]
sol = solution(test_key, test_lock)
print('solution', sol)