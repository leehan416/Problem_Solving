t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    floor = n % h
    if floor == 0:
        floor = h
        num = n//h
    else: num = n // h + 1
    print(floor * 100 + num)