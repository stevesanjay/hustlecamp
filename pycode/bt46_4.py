# Matching Specific Patterns (e.g., phone numbers):

import re

text = 'Call me at 123-456-7890 or 987.654.3210.'

phone_numbers = re.findall(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', text)
print('Phone numbers found:', phone_numbers)