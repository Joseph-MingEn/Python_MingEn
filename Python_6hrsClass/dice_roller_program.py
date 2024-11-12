import random

dice_art = {
    1: (
        "┌───────┐",
        "│       │",
        "│   ●   │",
        "│       │",
        "└───────┘",
    ),
    2: (
        "┌───────┐",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "└───────┘",
    ),
    3: (
        "┌───────┐",
        "│ ●     │",
        "│   ●   │",
        "│     ● │",
        "└───────┘",
    ),
    4: (
        "┌───────┐",
        "│ ●   ● │",
        "│       │",
        "│ ●   ● │",
        "└───────┘",
    ),
    5: (
        "┌───────┐",
        "│ ●   ● │",
        "│   ●   │",
        "│ ●   ● │",
        "└───────┘",
    ),
    6: (
        "┌───────┐", # 0
        "│ ●   ● │", # 1
        "│ ●   ● │", # 2
        "│ ●   ● │", # 3
        "└───────┘", # 4
    ),
}

run = input("請輸入'run'開始擲骰子:")
dice = [1, 2, 3, 4, 5, 6]
boxes = []
total = 0
if run == "run":
    for i in range(3):
        boxes.append(random.choice(dice))
        for j in range(5):
            print(dice_art[boxes[i]][j])
        total += boxes[i]

print(f"總和: {total}")
for i in range(3):
    for j in range(5):
            print(dice_art[boxes[i]][j])