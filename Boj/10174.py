for _ in range(int(input())):
    n=input()
    l=list(n)
    l.reverse()
    p="".join(l)
    if n.lower()==p.lower():
        print("Yes")
    else:
        print("No")