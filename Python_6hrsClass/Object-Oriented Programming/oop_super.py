#Super Function

class Rectengle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        print("Rectengle running...")

class Square(Rectengle):
    def __init__(self, width, length):
        super().__init__(width, length)
        print("Square running...")

class Cube(Rectengle):
    def __init__(self, width, length, height):
        super().__init__(width, length)
        self.height = height
        print("Cube running...")


cube = Cube(10 , 30, 50)

square = Square(10 , 30)