n, m = map(int, input().split())
out = 0
while True:
    out += 1 

    if n > m:
        out = -1
        break
    elif n == m:
        break

    if m % 10 == 1:
        m //= 10
    else:
        m /= 2
print(out)