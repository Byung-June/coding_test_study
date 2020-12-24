

def sol(p_list):
    x_1 = [p[0]for p in p_list]
    y_1 = [p[1]for p in p_list]
    z_1 = [p[2]for p in p_list]
    x_2 = [p[3]for p in p_list]
    y_2 = [p[4]for p in p_list]
    z_2 = [p[5]for p in p_list]

    x_a, x_b = max(x_1), min(x_2)
    y_a, y_b = max(y_1), min(y_2)
    z_a, z_b = max(z_1), max(z_2)

    if x_a > x_b:
        return 'NULL', 0
    else:
        result1 = max(0, x_b - x_a)
    if y_a > y_b:
        return 'NULL', 0
    else:
        result2 = max(0, y_b - y_a)
    if z_a > z_b:
        return 'NULL', 0
    else:
        result3 = max(0, z_b - z_a)
    result = [result1, result2, result3]
    if result.count(0) == 3:
        return 'POINT', 0
    elif result.count(0) == 2:
        result.remove(0)
        result.remove(0)
        return 'EDGE', result[0]
    elif result.count(0) == 1:
        result.remove(0)
        return 'FACE', result[0] * result[1]
    else:
        return 'VOLUME', result[0] * result[1] * result[2]




