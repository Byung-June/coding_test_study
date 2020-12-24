def solution(numbers):
    def make_str(num):
        temp = num * 4
        return int(temp[:4])

    numbers = [(num, make_str(str(num))) for num in numbers]
    numbers = sorted(numbers, key=lambda x: x[1], reverse=True)
    answer = ''
    for i, j in numbers:
        answer += str(i)
    return str(int(answer))

numbers = [6, 10, 2]
# numbers = [3, 30, 34, 5, 9]
numbers = [1000, 0, 5, 99, 100]
print(solution(numbers))