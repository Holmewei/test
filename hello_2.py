#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# _author_="songwei"

import getpass

username = input("name:")
password = getpass.getpass("password:")
if username == "tom" and password == "123":
    print("login")
else:
    print("bad")
