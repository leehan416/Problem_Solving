# 계속 고민하다 답지보고 풀었음
# 주기를 파악하니 쉽게 이해됨 ㅇㅇ
import sys
n = int(sys.stdin.readline())
mod = 1000000
p = mod//10*15 # 주기
l = [0,1]
for i in range(2, p):
    l.append(l[i-1] + l[i-2])
    l[i] %= mod
print(l[n%p])