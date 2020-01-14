import random
"""
Print a message to the console indicating whether each value of
`number` is in the `my_randoms` list.
"""


# A random list of 10 numbers is assigned to my_randoms
my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6))

# Generate a list of numbers 1..10
numbers_1_to_10 = range(1, 11)

"""
The first FOR loop goes through each sequential number. The next FOR loop goes through a the whole list of random numbers for each loop through the outer list. The IF comparator checks if the outer loop number is equal to any of the randomly-generated numbers. The following IF prints either message depending on the value of the boolean.
"""

# Iterate from 1 to 10
for number in numbers_1_to_10:
    the_numbers_match = False

# Iterate your random number list here
    for random_number in my_randoms:
        if number == random_number:
# Does my_randoms contain number? Change the boolean.
            the_numbers_match = True
    if the_numbers_match:
        print(f'{number} is in the random list')
    else:
        print(f'{number} is NOT in the random list')