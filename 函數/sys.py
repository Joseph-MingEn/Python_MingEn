import sys

# 印出命令行參數
print("命令行參數:", sys.argv)

#%%
import sys

# 重新導向標準輸出
sys.stdout = open('output.txt', 'w')

print("這將被寫入到 output.txt")

#%%
import sys

# 當發生某些條件時退出程序
if some_condition:
    sys.exit()

#%%
import sys

# 查看模塊搜索路徑
print("模塊搜索路徑:", sys.path)

#%%