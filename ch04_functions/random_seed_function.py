'''
use seed values to generate the same sequence of random numbers
'''

from random import seed, randrange

SEED_NUM = 32

for diceRoll in range(10):
    '''
    group 1
    - uses a random seed to generate 10 numbers and print them
    '''
    print(randrange(1,7), end=' ')

print("\n")

seed(SEED_NUM)     # sets the random seed number to SEED_NUM
for diceRoll in range(10):
    '''
    group 2
    - uses predetermined SEED_NUM as the seed number to generate 10 random numbers
    '''
    print(randrange(1,7), end=' ')

print("\n")

for diceRoll in range(10):
    '''
    group 3
    - uses a random seed to generate 10 numbers and print them
    - generates a different set of numbers from groups 1 and 2
    '''
    print(randrange(1,7), end=' ')

print("\n")

seed(SEED_NUM)
for diceRoll in range(10):
    '''
    group 4
    - uses the predetermined seed number to generate 10 random numbers
    - generates the same set of numbers as group 2
    '''
    print(randrange(1,7), end=' ')

print("\n")