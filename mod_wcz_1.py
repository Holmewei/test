#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# _author_="HolmeWei"
def wordCount(s):
    chars = len(s)
    words = len(s.split())
    lines = s.count('\n')
    print(lines,words,chars)

s = open("/etc/hosts").read()

if __name__ == '__main__':
    wordCount(s)
