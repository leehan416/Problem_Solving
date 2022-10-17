S = input()
l = [0,0]
for i in range(1, len(S)):
    value =  int(S[i - 1]) - int(S[i])
    if (value <= -1): # 01
        l[0] +=1  
    elif (value == 1):# 10
        l[1] += 1

print(max(l))