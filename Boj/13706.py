n=int(input())
left, right = 1, n
while right > left:
    mid = (left +right)//2
    if mid ** 2 ==n:
        right= mid
        break
    elif mid ** 2 >  n:  right = mid -1
    elif mid **2 < n: left=mid +1
print(right)