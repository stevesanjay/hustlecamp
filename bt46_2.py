# Extracting Email Addresses from Text:

import re

text = 'Contact me at email@example.com or info@example.org.'

emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print('Email addresses found:', emails)