import random

foodType = input("請選擇飯類、麵類、餃類、火鍋類: ")
if foodType == "飯類":
    weights = [20, 20, 40, 10, 30]
elif foodType == "麵類":
    weights = [30, 20, 20, 20, 50]
elif foodType == "餃類":
    weights = [50, 20, 10, 20, 10]
elif foodType == "火鍋類":
    weights = [20, 30, 40, 10, 10]

# set up prize and weight
prizes = ["八方雲集", "三媽臭臭鍋", "便當", "全家", "燉飯、義大利麵"]
# weights = [10, 20, 30, 40, 10]

print(len(prizes), len(weights))  # 确保这两者的长度相同

# calculate total weight

def draw_lottery():
    result = random.choices(prizes, weights, k=1)[0]
    return result

def simulate_deaws(n):
    results = {}

    for prize in prizes:
        results[prize] = 0

    for _ in range(n):
        result = draw_lottery()    
        results[result] += 1

    return results

num_draws = 17

draw_results = simulate_deaws(num_draws)

for prize, count in draw_results.items():
    print(f"{prize}: {count/num_draws*100:.2f}%")