n =int( input())
l=[]
for _ in range(n):
    l.append(input().split())
l.sort(key= lambda x:x[1])
print(l[0][0])

       