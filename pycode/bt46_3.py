# Replacing Patterns in a String:

import re

text = 'Hello, my name is Alice. Hello, my name is Bob.'

new_text = re.sub(r'Hello', 'Hi', text)
print('New text:', new_text)