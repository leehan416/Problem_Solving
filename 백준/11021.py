value = int(input())
l=[]

for _ in range(value):
  val = input().split()
  l+=[int(val[0] )+int(val[1])]

for i in range(len(l)):
  print("Case #"+str(i+1)+":", l[i]) 