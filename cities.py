
import sys
from faker import Faker

faker = Faker()


def random_cities():

    cities = []

    for i in range(10):

        city = faker.city()
        print(f"{city}")


random_cities()



# return cities

# print(f"{city:2d} : {pincode}")
        
#  print(f"{i:2d} x {num:2d} = {i * num:2d}")