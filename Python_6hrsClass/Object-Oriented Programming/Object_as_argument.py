#把物件作為引數

class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = "none"

def change_color(Dog, color):
    Dog.color = color

dog1 = Dog("Buddy", "brown")

print(dog1.color)

change_color(dog1, "black")

print(dog1.color)