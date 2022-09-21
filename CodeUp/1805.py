l = []
for _ in range(int(input())): l.append(list(map(int, input().split())))
for i in sorted(l): print(i[0], i[1])