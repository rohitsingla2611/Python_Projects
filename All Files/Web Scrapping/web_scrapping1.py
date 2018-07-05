import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
source_code = requests.get(url)
print('Source Code', source_code)

print('-------------------------------')
su = source_code.text
print(su)

print('--------------------------------------------------------------------')
code = BeautifulSoup(su, "html.parser")
print(code)

print('--------------------------------------------------------------------')
print(code.li)

print('--------------------------------------------------------------------')
print(code.text)

print('--------------------------------------------------------------------')
# print(code.index("<div>"))

print('--------------------------------------------------------------------')
code1 = code.findAll("div")
print(code1)

print('--------------------------------------------------------------------')
print(code.title.string)

print('--------------------------------------------------------------------')
code2 = code.findAll("div", {"class": "after-portlet after-portlet-lang"})
print(code2)

print('--------------------------------------------------------------------')
code3 = code.findAll(id="mw-head-base")
print(code3)
# i = 0
# for i in code:

#  if code.text
