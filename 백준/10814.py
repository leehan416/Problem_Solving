from operator import itemgetter
n =int(input())
l=[]
for _ in range(n):
  i = input()
  l+=[[int(i.split()[0]), i.split()[1]]]
l = sorted(l, key= itemgetter(0))
for i in l:
  print(i[0],i[1]) 