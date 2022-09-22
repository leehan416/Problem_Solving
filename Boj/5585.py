arr = [500, 100, 50, 10, 5, 1]
n = 1000 - int(input())
num = 0

for i in arr:
    num += n // i
    n %= i 
print(num)