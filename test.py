# -*- coding: utf-8 -*-
import re

txt = "百度网盘提取码：laod 解压密码：laod.org"
pwd_re = re.compile(r".+密码：(.+)$")
pwd = pwd_re.search(txt)
print pwd.group(1)
