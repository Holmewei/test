#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# _author_="HolmeWei"
class Dog:
    def __init__(self):
        self.name = '花花'
        self.leg = 4
        self.age = 3
        self.color = "B"
    def show(self):
        print("名字：%s，腿的数量：%s，年龄：%s，颜色：%s" %(self.name,self.leg,self.age,self.color))


dog1 = Dog()

dog1.show()

dog2 = Dog()

dog2.show()