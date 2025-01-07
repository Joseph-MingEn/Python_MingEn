#Lambda Function


# EX1(兩倍)
# 一般
def double(x): 
    return x * 2

print(double(5))

# Lambda
double2 = lambda x : x * 2

print(double2(50))

# EX2(相乘)
multiply = lambda x, y : x * y

print(multiply(5, 10))

# EX3(if else)

result = lambda x : f"{x}是偶數" if x % 2 == 0 else f"{x}是奇數"

print(result(10))

# EX4(字串)
full_name = lambda first_name, lest_name : f"{first_name} {lest_name}"

print(full_name("John", "Doe"))