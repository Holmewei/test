#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# _author_="HolmeWei"
import getpass
username = input("name:")
password = getpass.getpass("password:")
n = 0
while True:
      if username =='tom' or password =='123':
          print("登录成功")
          break
      else:
          n = n + 1
          print("登录失败%s次" %n)
      username = input("name:")
      password = input("password:")

      if n == 2:
          print("登录失败")
          break