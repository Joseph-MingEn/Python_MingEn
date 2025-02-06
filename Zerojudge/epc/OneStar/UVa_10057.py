while True:
    try:
        n = int(input())
        num = []
        counts = []
        Min = 100000000
        absMin = 100000000

        ans1 = []
        ans2 = 0
        ans3 = 0

        for i in range(n):
            num.append(int(input()))
        num = sorted(num)

        A = num[0] - 1

        for i in range(num[len(num) - 1] - num[0] + 1):
            A += 1
            # print("A =", A)
            count = 0
            for j in range(len(num)):
                count += abs(num[j] - A)
            counts.append(count)

            Min = min(Min, count)

        # print("Min =", Min, "Counts = ", counts)
        A = num[0] - 1

        for i in range(len(counts)):
            A += 1
            if counts[i] == Min:
                ans1.append(A)
                for j in range(len(num)):
                    absMin = min(absMin,abs(num[j] - A))

        absCount = 0
        A = num[0] - 1
        for i in range(len(counts)):
            A += 1
            if counts[i] == Min:
                for j in range(len(num)):
                    # print("abs(num[j] - A) = ", abs(num[j] - A))
                    if absMin == abs(num[j] - A):
                        absCount += 1
                        # print("absCount =", absCount)

        ans2 = absCount
        del absCount

        ans3 = len(ans1)

        # print("absMin =", absMin)

        print(int(ans1[0]), ans2, ans3)

    except EOFError:
        break
    except ValueError:
        break