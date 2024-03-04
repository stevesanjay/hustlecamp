
'''
Created on 

@author: Raja CSP Raman

source:
    https://stackoverflow.com/questions/370357/python-variable-scope-error
'''

from faker import Faker

faker = Faker()


def generate_names(limit):

    name_list = []
    for index in range(limit):
        c_name = faker.name()
        name_list.append(c_name)
    cleanup_list(name_list)
    # print(name_list)

    return name_list

def cleanup_list(abc):



def startpy():
    
    result = generate_names(10)
    print(result)

    new_result = cleanup_list(result)
    

if __name__ == '__main__':
    startpy()