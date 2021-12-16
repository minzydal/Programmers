def solution(arr):
    answer = []
    arr.remove(min(arr)) # 최소값 찾아서제거
    answer = arr # 최소값 제거 후 배열에 넣어줌
    if len(arr) < 2 : answer = [-1] # 배열 길이가 1이면 -1로 채워줌
    return answer