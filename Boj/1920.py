n = input()
a = list(map(int, input().split()))
m = input()
l = list(map(int, input().split()))
a.sort()

def search(f, b, n):
  if f > b: return 0
  m = (f + b) // 2 
  if a[m] == n: return 1
  elif n > a[m]: return search(m + 1, b, n)
  else: return search(f, m - 1, n)
    
for i in l:
  print(search(0, len(a)-1, i))