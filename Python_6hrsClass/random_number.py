import random
#randint
print(random.randint(1,10))

#random
print(random.random())

#列表中隨機一個元素
options = ["剪刀", "石頭", "布"]
random_options = random.choice(options)
print(random_options)

#將列表多個元素隨機組合
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(cards)
print(cards)

########################################################################
#猜數字遊戲
sol = random.randint(1,100)

Max = max(sol, 100)
Min = min(sol, 1)

while True:
    num = int(input(f"請輸入>{Min} and <{Max} 的值(整數):"))
    if num == sol: break
    else:
        if sol > num:
            Min = num
        else: 
            Max = num

print(f"sol={sol}")