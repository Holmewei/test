#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# _author_="Holmewei"

# sum = 0
# counter = 1
# while counter <= 100:
#     sum += counter
#     counter += 1
# print("result is %d" %(sum))

#age = int(input("请输入年龄:"))
for age in range(1,101):
    age = int(input("请输入年龄:"))
    if age >= 1 and age <18:
        print("年龄太小，属于未成年人")
    elif age >= 18 and age <= 50:
        print("属于成年人")
    else:
        print("属于老年人")
print(age)

