salary = int(input("請輸入薪資金額: "))
print("")
award = int(input("請輸入工作獎金: "))
print("")
workovertime = int(input("請輸入加班費: "))

total = salary + award + workovertime

print("本月實領金額為: %s" % (total))