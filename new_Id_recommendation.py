def solution(new_id):
    answer = ''
    #1 대문자 -> 소문자
    new_id = new_id.lower()
    #2 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자 제거
    for c in new_id :
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.'] :
            answer += c
    #3 마침표(..)가 2번 이상 연속된 부분을 하나의 (.)로 치환
    while '..' in answer :
        answer = answer.replace('..', '.')
    #4 마침표 (.)가 처음이나 끝에 위치한다면 제거
    if answer[0] == '.' :
        answer = answer[1:]
    elif answer[-1] == '.' :
        answer = answer[:-1]
    #5 answer가 빈 문자열일 때 'a'를 대입
    if answer == '' :
        answer = 'a'
    #6 길이가 16자 이상이면 15개 문자를 제외한 나머지 문자 모두 제거
    if len(answer) > 15 :
        answer = answer[:15]
    if answer[-1] == '.' :
        answer = answer[:-1]
    #7 길이가 2자 이하라면 길이가 3이 될 때까지 마지막 문자를 더함
    while len(answer) < 3 :
        answer += answer[-1]

    return answer