# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 09:37:16 2021

@author: Administrator
"""

a,b=1,0
while a<10:
    print(a)
    a,b=b,a+b
    #%%
fruit=['爆米花','banana','guava']
number=0
for food in fruit:
    number=number+1
    print("The food is",food,".")
    print(number)
    print('There are',len(fruit),'types of fruit')
    #%%
fruit=['apple','banana','guava']
number=0
for food in fruit:
    print("The food is",food,".")
    print('There are',len(fruit),'types of fruit')
    #%%
list1=['a','b','c']
print(list1)
for x in list1:
    print("The character is ",x,".")
    #%%
string="beautful"
for x in string:
    print(x)
    #%%
tuple5=('竹崎高中',2,'竹崎高中三年級二班1號')
print('tuple5為',tuple5)
print('tuple5[2]是',tuple5[2])
    #%% 
dict7={'同學':100,'2':2,'大學':80000}
print('dict7 為',dict7)
print("dict7['同學']的值",dict7['同學'])
print("dict7['大學']的值",dict7['大學'])
    #%%
dict7={'同學':100,'2':2,'大學':80000}
asking=input("請輸入詢問項目:")
print(dict7[asking])
