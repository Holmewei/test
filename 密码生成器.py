#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# _author_="HolmeWei"
import string
import random
import sys
def keygen(num):

    pwd = ''
    all_choice = string.ascii_letters + string.digits

    for i in range(8):
        pwd += random.choice(all_choice)

    print(pwd)

# if __name__ == '__main__':
# #   for i in range(int(sys.argv[2])):
#         keygen(int(sys.argv[1]))
keygen(8)