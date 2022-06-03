from collections import Counter

i = input()
l=Counter(input())
if l['A']>l['B']:
    print("A")
elif l['A'] <l["B"]:
    print("B") 
else:
    print("Tie")  