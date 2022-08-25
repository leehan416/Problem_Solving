set = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
num = input()
value = 1
for i in num:
    if i in set:
        set.remove(i)
    else:
        try:
            if i == '6':
                if '9' in set:
                    set.remove('9')
                    continue
                a = 1 / 0
            elif i == '9':
                if '6' in set:
                    set.remove('6')
                    continue
                a = 1 / 0   
            a = 1 / 0    
        except: 
            value += 1
            set += ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        set.remove(i)
print(value)