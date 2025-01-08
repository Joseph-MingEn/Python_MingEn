# 字典推導式

# dictionary = {key: expression(運算) for key, value in iterable}
# EX1
cities_in_F = {'LA': 120, 'New York': 65, 'Chicago': 50, "Miami": 150}
cities_in_C = {key: round((value - 32) * 5/9) for key, value in cities_in_F.items()}

print(cities_in_C)
print(cities_in_F)


# EX2 條件判斷
weather = {'台北': 'Good', '台中': 'Good', '宜蘭': 'Bad'}

good_weather_cities = {key: value for key, value in weather.items() if value == 'Good'}

print(good_weather_cities)


# EX3 條件判斷 + Function
cities_in_F = {'LA': 120, 'New York': 65, 'Chicago': 50, "Miami": 150}

def check_weather(temp):
    if temp >= 70:
        return 'Hot'
    else:
        return 'Cold'

weather_in_cities = {key: check_weather(value) for key, value in cities_in_F.items()}

print(weather_in_cities)