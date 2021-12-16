def solution(n):
    a = []
    sum = 0
    for i in range(1, n+1) :
        if n % i == 0 :
            a.append(i)
    for j in a :
        sum += j
    return sum