#作用域

#L > E > G > B 作用域順序

# 1. Local Scope: 區域
# 2. Enclosed Scope:
# 3. Global Scope: 全域
# 4. Built-in Scope:Python 內建的function

a = 10 #Global
print(a)

def function_one():
    x = 10

    a = 2

    print(x)
    def function_two():
        y = 30
        print(y) #Local for function_two
        #   nonlocal x; x = 20 #在函數內部訪問並修改外層（非全域）變數
        print(x)#Enclosed for function_two

        print(a)
    
    function_two()


function_one()

##
from math import e
print(e)# Built-in