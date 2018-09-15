#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# _author_="HolmeWei"
#取内存总量
f = open('/proc/meminfo','r')

for lines in f:
    if lines.startswith("MemTotal:"):
        memtotal = int(lines.split()[1]) / 1024
    if lines.startswith("MemFree:"):
        memfree = int(lines.split()[1]) / 1024
        break
print("Used:%.2f - %.2f = %.2f" %(memtotal ,memfree,memtotal - memfree))