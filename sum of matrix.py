def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)) :
        sum_arr = []
        for j in range(len(arr1[0])) :
            sum_arr.append(arr1[i][j] + arr2[i][j])
        answer.append(sum_arr)
    return answer