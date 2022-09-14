def solution(s):
    l=[]
    for i in s.split():
        l.append(int(i))      
    answer = str(min(l)) + ' ' + str(max(l))
    return answer