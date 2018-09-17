#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# _author_="HolmeWei"
import  mod_wcz_1

with open('etc/passwd') as f:
mod_wcz_1.wordCount(f.read())
