#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# _author_="HolmeWei"
import string
import random
import sys
def key_time(num):
    pwd = ''
    all_choice = string.ascii_letters + string.digits
    for i in range(8):
        pwd += random.choice(all_choice)
    print(pwd)

key_time(8)