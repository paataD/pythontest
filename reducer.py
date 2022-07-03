#!/usr/bin/python3.9

import random
import re
import sys

lines = []
count = 0
lineLength = random.randint(1, 5)
for line in sys.stdin:
    if count <= lineLength:
        count += 1
        lines.append(re.findall(r'^\S', line)[0])
        continue
    print(lines)
    lines = []
    lineLength = random.randint(1, 5)
