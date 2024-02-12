'''
Created on 

@author: Raja CSP Raman

source:
    https://stackoverflow.com/questions/370357/python-variable-scope-error
'''

def startpy():

    print("Tact101")

    item_list = [
        "a:12",
        "b:13"
    ]

    ghi = [
        1, 
        102, 
        22
    ]

    # int, float, string, list, dict, set, tuple

    # a:12
    abc = item_list[0]
    ijk = abc.split(":")[1]
    print(f"ijk : {ijk}")
    print(type(ijk))

    # 12
    # a_val = 
    print(f"item_list : {item_list[0]}")
    

if __name__ == '__main__':
    startpy()