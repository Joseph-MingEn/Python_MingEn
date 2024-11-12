goods = []
prices = []

#無窮迴圈
while True:
    good = input("輸入想買的物品:")
    if good == "end":
        break
    princ = input(f"輸入{good}價格:")
    goods.append(good)
    prices.append(princ)

#enumerate將一個可迭代的對象（如列表、元組或字串）轉換為索引序列，同時列出資料和資料對應的索引值。
for index, good in enumerate(goods):
    print(f"{index+1}. {good}: {prices[index]}")