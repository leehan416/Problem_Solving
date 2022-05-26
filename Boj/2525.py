h, m= map(int,input().split())
min = int(input())
m += min
while m >= 60 :
  m-= 60
  h+=1
  if h >= 24:
    h -=24
print(h,m)