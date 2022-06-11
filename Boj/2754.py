n = input()
l ={"A":4.0, "B":3.0, "C":2.0, "D":1.0, "F":0 }
value =0.0
if n[0] != "F":
    value+=l[n[0]]
    if n[1] == "+":
        value +=0.3
    elif n[1] == "-":
        value -= 0.3
print(value)