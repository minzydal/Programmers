def solution(n):
    a = list(str(n))
    sum = 0
    for i in range(len(a)) :
        sum += int(a[i])
    return sum