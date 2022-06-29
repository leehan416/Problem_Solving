l = []
d = dict()
for _ in range(int(input())):
    t = input().split()
    d[t[0]] = t[1]

for i in d.keys():
    if d[i] == "enter":
        l.append(i)

for i in sorted(l, reverse = True):
    print(i)