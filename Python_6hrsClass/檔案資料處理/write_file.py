# 新增文件
str = r"C:\Users\TUMINGEN\Documents\GitHub\pymingen\Python_6hrsClass\檔案資料處理\wirte_test.txt"

text = "hallo world!\nGood Luck!"

#'w' write 覆蓋撰寫
with open(str, 'w') as file:
    file.write(text)

#'a' 插入 插入撰寫
with open(str, 'a') as file:
    file.write("\nGo! Go!\tLet's Go!")