n =int( input())
l=[]
for _ in range(n):
  l+=[int(input())] 
l.sort()
for i in range(n):
  print(l[i])