#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# _author_="HolmeWei"
class  YunSuan:
    def __init__(self,passx,passy):
        self.x = passx
        self.y = passy
        self.he = 0
        self.cha = 0

    def sum(self):
       return "%s + %s = %s" %(self.x,self.y,self.x + self.y)
    def sub(self):
       return "%s - %s = %s" %(self.x,self.y,self.x - self.y)

one = YunSuan(9,3)

print(one.sum())




