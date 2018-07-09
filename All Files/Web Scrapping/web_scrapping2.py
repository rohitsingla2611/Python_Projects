import requests
from bs4 import BeautifulSoup

url = "https://epaper.timesgroup.com/Olive/ODN/TimesOfIndia/#"

url1 = "https://en.wikipedia.org/wiki/Python_(programming_language)"

url2 = "https://indianexpress.com/article/business/interpol-issues-red-corner-notice-against-nirav-modi-in-pnb-fraud-case-5242044/"

url3 = "https://www.indiatoday.in/business/story/shopkeepers-protest-walmart-flipkart-deal-citing-unfair-competition-1275878-2018-07-03"

source_code = requests.get(url3)
su = source_code.text
code = BeautifulSoup(su, "html.parser")
'''
# code1 = code.findAll(id="mw-head-base")

# print(code1)
print('==========================')

code2 = code.findAll("div", {"class": "info"})
print(code2)
print('==========================')

code3 = code.findAll("h1", {"class": "native_story_title"})
print(code3)
'''
print('==========================')

code4 = code.findAll("h1", {"itemprop": "headline"})

print(code4.format)
print('==========================')

code5 = str(code4)[25:-6]
print(code4)
print(code5)
code6 = code.findAll("p")
code7 = code.findAll(itemprop="articleBody")

code7 = code7.__str__.replace("<p>", "").replace("<>", "").replace(".", ".\n").replace("<div", "")
code7 = code7
code7 = code7
code7 = code7[49:-7]
print(code7)  # , end=".\n")

'''
for i in code7:
    print(i.string)
'''
