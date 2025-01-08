# time

# 系統的初始時間 epoch
import time

print(time.ctime(0))

# 取得現在的時間
print(time.time())

# 時間格式化
local_time = time.localtime()
print("時間格式化:", time.strftime("%Y-%m-%d %H:%M:%S", local_time))

time_string = "2021-01-01 12:00:00"

time_object = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")

print(time_object)