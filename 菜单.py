#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# _author_="HolmeWei"
#         for i in range(1,10):
#             for j in range(1,i+1):
#                 print("%s * %s =%s" %(j,i,i * j),end="  ")
#             print()

# x = ""
# while not x:
#     name = input("your name:")
#     age = input("your age:")
# print("name:%s age:%s" %(name,age))

x = ""
chioce ="""1.啤酒
2.白酒
3.矿泉水
请使用(1、2、3):
4.是
5.否
请选择是否退出(3、4):"""
while not x:
    print("请选择以下内容:")
    x = input(chioce)
    if x == '1':
        print("喝啤酒")
    elif x == '2':
        print("喝白酒")
    elif x == '3':
        print("喝矿泉水")
    elif x == '4':
        break
    elif x == '5':
        continue