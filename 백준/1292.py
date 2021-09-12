userInput = input()
firstNum = int(userInput.split(" ")[0])
secondNum = int(userInput.split(" ")[1])
result = 0
index = 0
for i in range(1, 1001):
    for j in range(i):
        index += 1
        if (firstNum <= index) and (index <= secondNum):
            result += i
        elif index > secondNum:
            break
print(result)