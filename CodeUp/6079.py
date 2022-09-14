i = int(input())
index=1
value = 0
while True:
    if value >= i: break
    else:
        value += index
        index += 1
print(index-1)