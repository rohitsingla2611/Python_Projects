import re

pat = "1111551222"
pat1 = "[0-9]+"
pat2 = "ab*"
pat3 = "[0-9]?"
pat4 = "ab*a+b?"
pat5 = "[]"

text = " My M.No. is 9988899911 is 1111551222 8847"
text2 = "a aaabbaab aab aa bb abababa bbbaaabaaa  ab ,aaaa 373777 7787 abbbaabb aabbaabbabababababbababa"

print('-----------------')
print(re.search(pat, text))

print('-----------------')
if re.search(pat1, text):
    print("Found")
else:
    print(" Not Found")

print('-----------------')
print(re.search(pat1, text))

print('-----------------')
print(re.findall(pat1, text))

print('-----------------')
print(re.findall(pat2, text2))

print('-----------------')
print(re.findall(pat4, text2))

print('-----------------')
'''

[0-9] individual number each
[^0-9] ^ not means it should not included


/s
/S
/d
/D
/w
/W
 




'''
