a = int(input("輸入a值: "))
b = int(input("輸入b值: "))

print("a = %d, b = %d" % (a, b))
##算術運算子
def arithmeticoperators (a, b):
    print("加            %d" % (a+b))
    print("減            %d" % (a-b))
    print("乘            %d" % (a*b))
    print("除            %d" % (a/b))
    print("除 取整數     %d" % (a//b))
    print("除 取餘數     %d" % (a%b))
    print("次方 a的b次方 %d" % (a**b))

##比較運算子
def comparisonoperator (a, b):
    print("a == b %s %d" % (a == b, a == b))
    print("a != b %s %d" % (a != b, a != b))
    print("a > b  %s %d" % (a > b, a > b))
    print("a < b  %s %d" % (a < b, a < b))
    print("a >= b %s %d" % (a >= b, a >= b))
    print("a <= b %s %d" % (a <= b, a <= b))

##邏輯運算子
def logicaloperators(a, b):
    c = int(input("輸入c值: "))
    d = int(input("輸入d值: "))
    print("c = %d, d = %d" % (c, d))
    print("not(a > b)  %s %d" % (not(a > b), not(a > b)))
    print("not(a < b)  %s %d" % (not(a < b), not(a < b)))
    print("(a > b) and (c > d) %s %d" % ((a > b) and (c > d), (a > b) and (c > d)))
    print("(a > b) and (c < d) %s %d" % ((a > b) and (c < d), (a > b) and (c < d)))
    print("(a < b) and (c > d) %s %d" % ((a < b) and (c > d), (a < b) and (c > d)))
    print("(a < b) and (c < d) %s %d" % ((a < b) and (c < d), (a < b) and (c < d)))
    print("(a > b) or (c > d) %s %d" % ((a > b) or (c > d), (a > b) or (c > d)))
    print("(a > b) or (c < d) %s %d" % ((a > b) or (c < d), (a > b) or (c < d)))
    print("(a < b) or (c > d) %s %d" % ((a < b) or (c > d), (a < b) or (c > d)))
    print("(a < b) or (c < d) %s %d" % ((a < b) or (c < d), (a < b) or (c < d)))

##複合指定運算子
def compoundspecifiedoperator(a, b):
    i = a
    i += b
    print("加 a += b     %d" % (i))
    i = a
    i -= b
    print("減 a -= b     %d" % (i))
    i = a
    i *= b
    print("乘 a *= b     %d" % (i))
    i = a
    i /= b
    print("除 a /= b     %d" % (i))
    i = a
    i %= b
    print("除 取整數 a %= b %d" % (i))
    i = a
    i //= b
    print("除 取餘數 a %= b %d" % (i))
    i = a
    i **= b
    print("次方 a的b次方 a **= b %d" % (i))

## () >> ** >> *, /,  %, // >> +, - >> ==, != ,>, <, 
arithmeticoperators (a, b)
comparisonoperator (a, b)
logicaloperators (a, b)
compoundspecifiedoperator (a, b)