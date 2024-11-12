def say_hello(string):
    print("Hello %s" % string)

say_hello("World")

def add(x, y):
    return x + y
x = add(3, 4)
print(x)
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return "%s %s" % (first, last)
name = create_name("aSd", "qwe")
print(name)