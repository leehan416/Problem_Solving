import sys
num = int(sys.stdin.readline())
stack = []
for _ in range(num):
  value = str(sys.stdin.readline())
  code = value.split()
  if code[0] == "push":
    stack.append(value.split()[1])
  elif code[0] == "pop":
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[-1])
      stack.pop()
  elif code[0] == "size":
    print(len(stack))
  elif code[0] == "empty":
    if len(stack) == 0:
      print(1)
    else:
      print(0)
  elif code[0] == "top":
    if len(stack)!= 0:
      print (stack[-1])
    else:
      print(-1)