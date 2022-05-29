def rev(n)->int:
  l=list(str(n))
  l.reverse()
  return int("".join(l))
x, y= map(int, input().split())
print(rev(rev(x)+rev(y )))