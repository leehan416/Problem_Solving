n = int(input())
l=[]
for _ in range(n):
    value = list(map(int, input().split(",")))
    l.append(sum(value))
for i in l:
    print(i)