n = ' '
n = n + input()
index = 1
while True:
    if index >= len(n): break
    print(n[index], end = '')
    if index != 0 and index % 10 == 0: print("")
    index += 1
