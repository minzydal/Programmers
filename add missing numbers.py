def solution(numbers):
    answer = 0
    num = range(0, 10)
    for i in num :
        if i not in numbers :
            answer += i
    return int(answer)