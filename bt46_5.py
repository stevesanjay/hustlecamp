# Splitting a String Based on a Pattern:

import re

text = 'Words, words, words, everywhere!'

words = re.split(r'\W+', text)
print('Words:', words)