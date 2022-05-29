import math
value = 0
n = str(math.factorial(int(input())))
for i in range(len(n)-1, -1, -1): 
  if n[i] == "0": value += 1
  else: break
print(value)