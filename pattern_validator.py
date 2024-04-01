'''
Created on 

@author: Raja CSP Raman

source:
    https://chat.openai.com/c/65ebd6c9-8acd-45d6-a194-370c0b6d1738
'''
import sys
import re

def validate_pattern(pattern_num, input_string):
    patterns = {
        '1': r'\d+\s+[a-zA-Z]+\s+[a-zA-Z]+',
        '2': r'\d{3}-\d{3}\s+[a-zA-Z]+\s+[a-zA-Z]+',
        '3': r'[a-zA-Z]+\s+\d+\s+[a-zA-Z]+'
    }
    
    if pattern_num not in patterns:
        print(f"Invalid pattern number: {pattern_num}")
        return
    
    pattern = patterns[pattern_num]
    
    if re.match(pattern, input_string):
        print(f"Pattern{pattern_num} matched")
    else:
        print(f"Pattern{pattern_num} NOT matched")
def startpy():

    # print("Tact101")
    if __name__ == "__main__":
        if len(sys.argv) != 3:
            sys.exit(1)
    
    pattern_num = sys.argv[1]
    input_string = sys.argv[2]
    
    validate_pattern(pattern_num, input_string)


if __name__ == '__main__':
    startpy()