# 10:24 ~

def solution(bridge_length, weight, truck_weights):
    answer = 0
    cur_weight = 0
    going = []
    for truck in truck_weights:
        # print('truck',truck, answer)
        while True:
            answer += 1
            going = [(x + 1, y) for (x, y) in going]
            # print('state',answer, going, cur_weight)
            if len(going) > 0:
                if going[0][0] >= bridge_length:
                    cur_weight -= going[0][1]
                    going.pop(0)

            if cur_weight + truck <= weight:
                cur_weight += truck
                going.append((0, truck))
                # print('truck', truck, answer)
                break
    answer += (bridge_length - going[-1][0])
    return answer


bridge_length = 2
weight = 10
# truck_weights = [10,10,10,10,10,10,10,10,10,10]
truck_weights = [7,4,5,6]
ans = solution(bridge_length, weight, truck_weights)
print(ans)
