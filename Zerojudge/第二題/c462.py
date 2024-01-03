k = int(input())
az = str(input())
ans = 0
seg = []
tmp = 1

for i in range(len(az)):
    if i == 0: i = 1
    if az[i].isupper() == az[i-1].isupper():
        tmp += 1
    else:
        seg.append(tmp)
        tmp = 1
    
    if tmp != 0:
        seg.append(tmp)
    
    tmp = -1

    for i in range(len(seg)):
        if seg[i] == k:
            if tmp == -1:
                tmp = i
            else:
                continue
        else:
            if tmp == -1:
                continue
            else:
                num = i - tmp
                if seg[i] > k:
                    num += 1
                if tmp != 0 & seg[tmp-1] > k:
                    num += 1
                ans = max(ans, num)
                tmp = -1

if tmp != -1:
    num = len(seg) - tmp
    if tmp != 0 & seg[tmp-1] > k:
        num += 1
    ans = max(ans, num)

print(ans*k)

