import sys
num =int(sys.stdin.readline())
queue =[]
for _ in range(num):
  value = str(sys.stdin.readline())
  code = value.split()
  if code[0] == "push":
    queue.insert(0, code[1])
  elif code[0] == "pop":
    if len(queue )  ==0:
      print(-1)
    else:
      print(queue[-1])
      queue.pop(-1)
  elif code[0] == "size" : 
    print(len(queue))
  elif code [0] == "empty":
    if len(queue) == 0:
      print(1)
    else:
      print(0)
  elif code[0] == "front":
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[-1])
  elif code[0] == "back":
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[0])