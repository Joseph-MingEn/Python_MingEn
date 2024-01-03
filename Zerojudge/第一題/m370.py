a, b = map(int,input().split())
c = list(map(int,input().split()))
c.sort()
r = [i for i in c if i >= a]
l = [i for i in c if i < a]
if len(r) > len (l): print(len(r), r[len(r) - 1])
else: print(len(l), l[0])