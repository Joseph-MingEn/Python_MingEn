# 物件(Object)是類別(Class)的實例(Instance)

# car 4 個輪子
# car.bow()

# 車 => Class
# 每台生產出來的車子 => 物件Object

class Car:
    def __init__(self, make, model, year, color):
        #初始化
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    
    def drive(self):
        print(self.model + "\tCar is driving")

    def stop(self):
        print(self.model + "\tCar is stopping")



car1 = Car("Toyota", "ALtis", 2021, "Blue")
car2 = Car("Ford", "Kuga", 2020, "Green")

print(car1.make)
print(car1.model)
print(car1.year)
print(car1.color)

car1.drive()