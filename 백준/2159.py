while True:
  n = input()
  if n == "0":
    break
  else:
    l = list(n)
    l.reverse()
    if list(n) == l:
      print("yes")
    else:
      print("no")