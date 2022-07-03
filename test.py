import re

st = 'A Interface'
first = re.findall(r'^\S', st)[0]
print(first)
