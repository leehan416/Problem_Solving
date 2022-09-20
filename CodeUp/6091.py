a,b,c = map(int, input().split())
value = 2

while True:
    if (value % a == 0)  and (value % b == 0) and (value % c == 0): break
    value+=1
print(value)