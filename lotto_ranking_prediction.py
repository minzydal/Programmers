def solution(lottos, win_nums):
    count = lottos.count(0)
    if count != 0: lottos.remove(0)

    cnt = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1

    best = 7 - (cnt + count)
    if best > 6: best = 6
    worst = 7 - cnt
    if worst > 6: worst = 6

    answer = [best, worst]
    return answer