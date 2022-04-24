value = int(input())
l=[]
s=[]
for _ in range(value):
  val = input().split()
  s+= [[val[0],val[1]]]
  l+=[int(val[0] )+int(val[1])]

for i in range(len(l)):
  print("Case #"+str(i+1)+":", s[i][0],"+",s[i][1],"=", l[i]) 