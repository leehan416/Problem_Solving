n = int(input())
for i in range(1, n+1):
    print(str(i)+' ' if i % 3 != 0 else '', end='')