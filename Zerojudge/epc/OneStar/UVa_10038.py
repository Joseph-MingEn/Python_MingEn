while True:
    try:
        List = list(map(int, input().split()))
        # print(List)
        isError = False
        Difference = []

        for i in range(len(List) - 2):
            j = i + 2

            if abs(List[j] - List[j - 1]) >= List[0] or abs(List[j] - List[j - 1]) == 0:
                isError = True

            Difference.append(abs(List[j] - List[j - 1]))


        Difference = sorted(Difference)
     
        if isError == False:
            for i in range(len(Difference)):
                # print(Difference[i], i + 1)
                if (i + 1) != Difference[i]:
                    isError = True

        if isError == False:
            print("Jolly")


        if isError == True:
            print("Not jolly")
        
    except EOFError:
        break