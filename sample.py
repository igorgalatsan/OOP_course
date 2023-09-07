import urllib.request
import re

html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()

data = re.findall("<!--(.*?)-->", html, re.DOTALL)[-1]
print("".join(re.findall("[A-Za-z]", data)))



# data =  set()
# with open('text.txt') as f:
#     for i in f.read():
#         data.add(i)
# print(list(data))
# a = "".join(map(str,data))
# print(a)
# #"".join(re.findall("[A-Za-z]", data))