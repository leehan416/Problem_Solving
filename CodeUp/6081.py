num = int(input(), 16)

for i in range(1, 16):
    print('%X'%num, '*%X'%i, '=%X'%(num*i), sep='')