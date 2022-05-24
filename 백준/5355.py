for i in range(int(input())):
  l = input().split()
  val = float(l[0])
  for i in (l[1:]):
    if i == "@":
      val*=3
    elif i == "%":
      val +=5
    elif i== "#":
      val -=7
  print ("%.2f" % val)