#!/usr/bin/python3.9
import sys
import random

lines = []
with open('sample') as f:
    lines = f.readlines()

count = 0
for line in lines:
    print(f'{random.random()} {line}')
