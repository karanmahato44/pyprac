# import my_module as mm
from my_module import find_index, foo

import sys
import random
import datetime
import os
import antigravity





langs = ['js', 'py', 'c', 'java', 'go', 'swift', 'dart']


index = find_index(langs, 'dart')
print(f'index of target is: {index}')
print(foo)

# print(sys.path)

random_choice = random.choice(langs)
print(f'random choice = {random_choice}')


print(datetime.datetime.now())
print(os.getcwd())
print(os.__file__)