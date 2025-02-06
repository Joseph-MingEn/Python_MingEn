n = int(input())

t = []
s = []

for i in range(n) :
    a, b = map(int, input().split())
    t.append(a)
    s.append(b)

M = -10
m = 110
error = 0
recode = 0

for i in range(n):
    if s[i] > M :
        M = s[i]
        recode = t[i]
    if s[i] == -1 : error = error + 1

total = M-n-(2*error)
if total < 0 :
    total = 0
print(total, recode)