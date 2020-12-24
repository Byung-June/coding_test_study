def solution(routes):
    answer = 1
    routes.sort()
    cam = routes[0][1]
    for car in routes:
        if car[0] <= cam:
            cam = min(cam, car[1])
        else:
            answer += 1
            cam = car[1]
    return answer