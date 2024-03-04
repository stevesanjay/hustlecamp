'''
Created on 

@author: Raja CSP Raman

source:
    https://stackoverflow.com/questions/370357/python-variable-scope-error
'''

import random
import sys
from faker import Faker

faker = Faker()

def generate_team(team_list, t_team_count):

    #divide into two
    each_team_size = int((len(team_list))/t_team_count)
    print(f"each_team_size: {each_team_size}")
    if(each_team_size == 0):
        return None

    new_team_list = []
    #sublist
    # first_team =["ajay","ram"]
    # second_team =["akhil","surya"]

    # new_team_list.append(first_team)
    # new_team_list.append(second_team)

    for idx in range(t_team_count):
        c_team =[]

        for midx in range(each_team_size):
            c_team_member = random.choice(team_list)
            c_team.append(c_team_member)

            team_list.remove(c_team_member)

        new_team_list.append(c_team)          


    # print(new_team_list)
    return new_team_list


def startpy():

    team_list =[]

    members_count = int(sys.argv[1])
    
    for idx in range (members_count):
        team_list.append(faker.name())
    # print(team_list)
    #count
    t_team_count = 4

    result = generate_team(team_list, t_team_count)
    print(result)
  
    
    

    #print("Tact101")
    

if __name__ == '__main__':
    startpy()


