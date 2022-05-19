l= [0]*91
def fibo(n): 
  if l[n]!=0:
    return l[n]
  if n == 0:
    return 0
  elif n <= 2:
    return 1
  else:
    l[n]= fibo(n-1)+fibo(n-2)
    return l[n]
print(fibo(int(input())))