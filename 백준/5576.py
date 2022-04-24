n1 = []
n2 = []

for _ in range(10):
  n1 += [int(input())]
for _ in range(10):
  n2 +=[int(input())]
n1.sort()
n2.sort()

print(n1[9]+ n1[8]+ n1[7], n2[9] + n2[8]+ n2[7])