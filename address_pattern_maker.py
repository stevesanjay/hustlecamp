'''
Created on 

@author: Raja CSP Raman

source:
    https://stackoverflow.com/questions/370357/python-variable-scope-error

'''

import sys

def input_file(filename):
    line_list =[]
    with open(filename, 'r') as file:
        for line in file:
            line_list.append(line.strip())
    return line_list


def create_pattern_7():
    line_list = input_file('/Users/tactlabs2/tact/datasets/cner-address/patterns/pattern7.txt')

    with open("pattern7-input-training.txt",'a') as f:
        for c_line in line_list:

            word = c_line.split()

            content = word[0]+'\t'+"STREET_NAME"
            content +='\n'+word[1]+'\t'+"HOUSE_NO"
            content += '\n'* 2

            # print(f'added{c_line}')

            f.write(content)
    # print("done pattern 7")

def create_pattern_8():
    '''
    sample = put brodarice 12
    
    put   STREET_NAME
    brodarice    STREET_NAME
    44  HOUSE_NO  
    '''
    line_list = input_file('/Users/tactlabs2/tact/datasets/cner-address/patterns/pattern8.txt')

    with open("pattern8-input-training.txt",'a') as fl:
        for c_line in line_list:
            word = c_line.split()

            content = word[0]+'\t'+"STREET_NAME"
            content += '\n'+word[1]+'\t'+"STREET_NAME"
            content += '\n'+word[2]+'\t'+"HOUSE_NO"
            content += '\n' * 2

            fl.write(content)
            




def startpy():
    pattern_no = int(sys.argv[1])

    if(pattern_no == 7):
        create_pattern_7()
    if(pattern_no == 8):
        create_pattern_8()
        # create_pattern_8()

        

    

    # print("Tact101")
    

if __name__ == '__main__':
    startpy()
    



'''
how to run?
py address_pattern_maker.py 7
'''