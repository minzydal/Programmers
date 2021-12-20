def solution(s):
    a = s.split(" ")
    result = ''
    for word in a :
        for i in range(len(word)) :
            if i % 2 == 0 : result += word[i].upper()
            else : result += word[i].lower()
        result += ' '
    return result[:-1]