try:
    x = int(input("請輸入一個整數:"))
    y = int(input("請輸入另一個整數:"))
    print(x/y)
# except ValueError:
#     print("請輸入整數")
# except ZeroDivisionError:
#     print("除數不為零")
except (ValueError, ZeroDivisionError):
    print("輸入錯誤")
else:
    print("No errors")
    
finally:
    print("不論如何，都會執行")