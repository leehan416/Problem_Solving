l =[]
d = {"Q1": 0,"Q2": 0,"Q3": 0,"Q4": 0,"AXIS": 0}
for i in range (int(input())):
    x, y = map (int, input().split())
    if x == 0 or y == 0: d["AXIS"] += 1
    elif x > 0 and y > 0: d["Q1"] += 1
    elif x < 0 and y > 0:  d["Q2"] += 1
    elif x < 0 and y < 0: d["Q3"] += 1
    else: d["Q4"] += 1

for i in range(len(d)):
    print(list(d.keys())[i]+":", list(d.values())[i])

    
