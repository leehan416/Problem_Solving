userInput = input()
num1 = int(userInput.split(" ")[0])
num2 = int(userInput.split(" ")[1])
value1= num1
value2 = num2
max = -1
while value2 != 0:
    value = value1 % value2
    value1 = value2
    value2 = value
print(value1)
print((num1*num2)//value1)
