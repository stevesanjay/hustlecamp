# Matching a Pattern in a String:

import re

pattern = r'apple'
text = 'I love apples and bananas.'

if re.search(pattern, text):
    print('Pattern found!')
else:
    print('Pattern not found.')