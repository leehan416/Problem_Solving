n = int(input())
l = list(map(int, input().split()))
out = [0 for i in range(23)]
for i in range(1, 24):
    for j in l:
        if i == j: out[i-1]+=1
for i in out:
    print(i, end= ' ')