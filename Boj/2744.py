text=input()
l=""
for i in text:
    if "a"<= i and i<="z":
       l+= i.upper()
    else :
        l+=i.lower()
print(l)