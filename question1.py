#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# _author_="HolmeWei"
s_file = input("请输入要备份的文件路径：")
d_file = input("请输入要备份的位置：")
s_ob_file = open(s_file,'rb')
d_ob_file = open(d_file,'wb')
while True:
     data = s_ob_file.readline()
     if not data:
         break
     d_ob_file.write(data)
s_ob_file.close()
d_ob_file.close()