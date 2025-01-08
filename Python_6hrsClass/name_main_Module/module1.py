# Python 中 if __name__ == '__main__':
import module2

module2.hello()

print("Module 1 __name__ = " + __name__)

if __name__ == '__main__':
    print('Module 1 __name__ == __main__')