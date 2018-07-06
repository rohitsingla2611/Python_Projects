import re

pat = "1111551222"
pat1 = "[0-9]+"
text = " My M.No. is 9988899911 is 1111551222"

print('-----------------')
print(re.search(pat, text))

print('-----------------')
if re.search(pat1, text):
    print("Found")
else:
    print(" Not Found")

print('-----------------')
if re.search(pat1, text):
    print(re.search(pat1, text))
