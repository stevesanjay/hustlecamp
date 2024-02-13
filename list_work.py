'''
Created on 

@author: Raja CSP Raman

source:
    https://stackoverflow.com/questions/370357/python-variable-scope-error
'''
import random
from faker import Faker

faker = Faker()

def generate_random_name(limit):
    """
    generate random names using faker library
    
    parameter:
    limit(int)
    """
    with open('name.txt', 'a') as f:
        for i in range(100):
            fake_name = faker.name()
            print(fake_name)
            f.write(fake_name + '\n')

            
    

def startpy():

    generate_random_name(3)

    #  11. Team Allocation (2 - 10 members)
    # num_members = random.randint(2,10)
    # print("no of team members:", num_members)

    #print("Tact101")

 
    # my_list = ["London","Paris","Rome","New york","Tokyo", "Madurai", "Coimbatore"]

    #1.accessing element by it index value
    # print(my_list[2])


    #2.access item by name matching

    # name_to_match = "London"
    # for place in my_list:
    #    if place == name_to_match:
    #        print("Found:", place)
    #        break
    # else:
    #       print("Name not found in the list.")



    #3.LENGHT OF LIST
    # lenght = len(my_list)
    # print(lenght)

    #4.REVERSE
    # my_list.reverse()
    # print(my_list)

    #5.CHOOSE RANDOM ITEM IN LIST
    # random_item = random.choice(my_list)
    # print("Random item:", random_item)

    #6.LAST SECOND(slice)
    # slice1 = my_list[-2]
    # print(slice1)

    #7.LAST VALUE
    #print("last value:",my_list[-1])

    #8.FIRST VALUE
    #print("first value:",my_list[0])

    #9.REMOVE BY INDEX
    #removed_item = my_list.pop(2)
    #print("Removed item:", removed_item)  
    #print("Updated list:", my_list)        


    #10.REMOVING BY ITEM NAME IN LIST
    #my_list.remove("London")
    #print(my_list)

    # https://chat.openai.com/share/d9e65151-a5ac-4549-aae1-2a6dea57479b


#The following illustrates how to write a string to a text file:



if __name__ == '__main__':
    startpy()