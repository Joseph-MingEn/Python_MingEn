menu = {
    "pizza" : "300",
    "burger" : "400",
    "ice cream" : "500",
    "salad" : "150",
    "steak" : "700",
    "chicken" : "600",
    "pasta" : "350"
}
print("menu:")
for item, price in menu.items():
    print(f"{item}: {price} 元")
cart = []
total = 0
while True:
    food = input("請輸入食物名稱:")
    if food == "end":
        break
    elif menu.get(food) is None:
        print("無此食物!")
        continue
    else:
        cart.append(food)
        print(f"{food} 已加入食物!")
        total += int(menu.get(food))
        
print(f"您的食物共:{total}元")