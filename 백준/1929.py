import sys
m, n = map(int, sys.stdin.readline().split())

def isPrime(n):
  for j in range (2, int(n **0.5) + 1, 1):
    if n % j == 0: return 0
  return 1

for i in range(m ,n + 1):      
  if i == 1:
    continue
  elif i == 2:
    print(i)
  else:
    if (isPrime(i)):
      print (i)
  