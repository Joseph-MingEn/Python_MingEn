#Method chining方法鏈

class Car:
    def turn_on(self):
        print("Car is turning on")
        return self
    
    def drive(self):
        print("Car is driving")
        return self
    
    def stop(self):
        print("Car is stopping")
        return self
    
    def turn_off(self):
        print("Car is turning off")
        return self
    
car = Car()

#Method chining
car.turn_on().drive().stop()