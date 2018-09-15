#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# _author_="Holmewei"
for i in range(10):
    if i==3:
        continue
    if i==5:
        break
    print(i)
else:
    print("main end")
