# Creating a list of tuples containing both number and its squared value:

numbers = [1, 2, 3, 4, 5]
number_squared_tuples = [(x, x**2) for x in numbers]
print(number_squared_tuples)