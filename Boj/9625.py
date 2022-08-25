a = 1
b = 0
num = int(input())
for _ in range(num):
    c = a
    a = b
    b += c
print(a,b)