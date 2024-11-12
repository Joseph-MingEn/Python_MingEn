import time

my_time = int(input("請輸入秒數:"))

for i in range(my_time):
    print(i + 1, "seconds")
    time.sleep(1)
print("end")