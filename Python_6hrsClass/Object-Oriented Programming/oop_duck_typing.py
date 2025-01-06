#Duck typing

class Duck:
    def walk(self):
        print("Duck walking")

    def talk(self):
        print("Duck talking")

class Dog:
    def walk(self):
        print("Dog walking")

    def talk(self):
        print("Dog talking")

#沒有繼承關係，但同一類型當作相同類別使用
class Human():
    def catch(self, duck):
        duck.walk()
        duck.talk()

human = Human()
dog = Dog()

human.catch(dog)