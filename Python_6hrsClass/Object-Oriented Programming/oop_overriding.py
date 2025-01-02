#Python 中的方法重寫(Method Overriding)

class Anime:
    def eat(self):
        print("Anime is eating")

class Rabbit(Anime):
    def eat(self): #重寫
        print("Rabbit is eating carrots")

anime = Anime()
anime.eat()

rabbit = Rabbit()
rabbit.eat()

# CASE 2

class Mammal(Anime):
    def hi(self):
        print("Mammal is saing(hi)")
    pass

class Cat(Mammal):
    def eat(self):
        print("Cat is eating fish")

class Dog(Mammal):
    def eat(self):
        print("Dog is eating bones")

cat = Cat()
dog = Dog()

cat.eat()
dog.eat()