N = int(input())
for i in range(N):
    L = int(input())
    List = []
    List = list(map(int, input().split()))
    sortList = sorted(List)
    count = 0
    total = 0
    while List != sortList:
        if count == len(List) - 1:
            count = 0
        # print(count)
        if List[count] > List[count + 1]:
            tump = List[count + 1]
            List[count + 1] = List[count]
            List[count] = tump
            total += 1
        else:
            count += 1
    
    print("Optimal train swapping takes", total, "swaps.")