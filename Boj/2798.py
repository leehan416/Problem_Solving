n, m = map(int, input().split())
l=list(map(int, input().split()))
value=0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            val =l[i] +l[j]+l[k]
            if val <= m and val> value:
                value= val
print(value)