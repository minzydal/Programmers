def solution(s):
    a = s.count('P') + s.count('p') # 대문자, 소문자 p 의 개수
    b = s.count('Y') + s.count('y') # 대문자, 소문자 y 의 개수
    if a == b : return True
    else : return False