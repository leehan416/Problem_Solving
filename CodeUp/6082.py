num = int(input())

for i in range(1, num + 1): 
    j = str(i)
    if '3' in j or  '6' in j or '9' in j: print("X", end='')
    else: print(j, end='')
    print('', end=' ')