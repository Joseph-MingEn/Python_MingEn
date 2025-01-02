# OOP - Python中的繼承

#父類別
class Animal:
    aLive = True

    def eat(self):
        print("Animal is eating.")

    def sleep(self):
        print("Animal is sleeping.")

#Animal類別的子類別
class Rabbits(Animal): #繼承
    def jump(self):
        print("Rabbit is jumping.")

animal = Animal()
rabbit = Rabbits()

animal.eat()

rabbit.jump()
rabbit.eat() #繼承

class Fish(Animal): #繼承
    def swim(self):
        print("Fish is swimming.")


class Hank(Animal): #繼承
    def fly(self):
        print("Hail is fling.")

fish = Fish()
hank = Hank()

fish.swim()
hank.fly()