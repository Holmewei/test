#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# _author_="HolmeWei"
class Dog:
    def __init__(self,name,leg,age,color):
        self.name = name
        self.leg = leg
        self.age = age
        self.color = color
    def show(self):
        return("名字：%s，腿的数量：%s，年龄：%s，颜色：%s" %(self.name,self.leg,self.age,self.color))


dog1 = Dog("花花","4",3,"B")

print("第一条狗:" +dog1.show())

dog2 = Dog("黑狮","3",5,"W")

print("第二条狗:" ,dog2.show())