def main():
    # 各科成績
    scores = [42.32, 37.18, 81.07, 81.22, 79, 70, 38]
    subjects = ['國文', '英文', '主修', '副修', '樂理', '視唱', '聽寫']
    total_score = 0
    discipline = 0
    discipline_weight = 0
    technical = 0
    technical_weight = 0

    # 輸入權重，並確保輸入正確
    weights = []
    for subject in subjects:
        while True:
            try:
                weight = float(input(f"請輸入{subject}的權重: "))
                if weight < 0:
                    print("權重不能為負數，請重新輸入！")
                    continue
                weights.append(weight)
                break
            except ValueError:
                print("請輸入有效的數字！")

    proportions = []
    for i in range(2):
        while True:
            try:
                proportion = float(input(f"請輸入{i}的權重: "))
                if proportion < 0:
                    print("權重不能為負數，請重新輸入！")
                    continue
                proportions.append(proportion / 100)
                break
            except ValueError:
                print("請輸入有效的數字！")

    print(proportions)

    # 計算加權後的成績
    for i in range(len(scores)):
        if i < 2:
            discipline += scores[i] * weights[i]
            discipline_weight += weights[i]
        else:
            technical += scores[i] * weights[i]
            # print(technical)
            technical_weight += weights[i]
            
    print(f"學科成績: {discipline}, 技術成績: {technical}")
    try:
        discipline = (discipline / discipline_weight) * proportions[0]
    except ZeroDivisionError:
        discipline = 0
    try:
        technical = (technical / technical_weight) * proportions[1]
    except ZeroDivisionError:
        technical = 0
    total_score = discipline + technical

    print(f"總分: {total_score: .2f}")

if __name__ == "__main__":
    main()