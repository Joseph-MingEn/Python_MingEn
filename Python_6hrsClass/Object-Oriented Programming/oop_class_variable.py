class Car:
    #類別變數
    wheel = 4 
    # 物件變數
    def __init__(self, make, model, year, color):
        #初始化
        self.make = make
        self.model = model
        self.year = year
        self.color = color


car1 = Car("Toyota", "ALtis", 2021, "Blue")
print(car1.model)
print(car1.wheel)

car2 = Car("三陽", "勁戰", 2020, "White")
car2.wheel = 2
print(car2.model)
print(car2.wheel)
