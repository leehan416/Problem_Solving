userInput = input()
month = int(userInput.split(" ")[0])
day = int(userInput.split(" ")[1])
a = ""
value = 0

for mon in range(1, month):
    if mon == 2:
        value += 28
    elif ((mon % 2 == 0) and mon <= 6) or ((mon % 2 == 1) and mon >= 9):
        value += 30
    else:
        value += 31

value = (value + day) % 7

if value == 0:
    a = "SUN"
elif value == 1:
    a = "MON"
elif value == 2:
    a = "TUE"
elif value == 3:
    a = "WED"
elif value == 4:
    a = "THU"
elif value == 5:
    a = "FRI"
else:
    a = "SAT"
print(a)
