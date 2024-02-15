# import random

# random_number = random.randint(1,20)
# print(random_number)

from faker import Faker

faker = Faker()
random_names = faker.name()
print(random_names)
