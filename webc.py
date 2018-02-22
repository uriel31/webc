#!/usr/bin/python3

import requests


print("""\033[92m
__      __ ___  ___   ___
\ \    / /| __|| - \ / _/
 \ \/\/ / | __|| _ | | |_
  \_/\_/  |___||___/ \___\\
\033[0m
--------------
WEB PAGE PWN3D
--------------
code  : python3
terit : space
github: https://github.com/uriel31/webc
""")
print("""\033[43mCRAFTED BY \033[41m Musthafa \033[0m\n""")
site = input("site name  :")
optName = input("output name:")
p = optName+".html"
r = requests.get("http://"+site)
t = open(p,'w')
t.write(r.text)
t.close()
print("success..!")
