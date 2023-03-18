'''
Roll a die a number of times and record the frequency of each number rolled
'''

from random import randint

TOTAL_DIE_ROLLS = 600_000

freq1Rolled = 0
freq2Rolled = 0
freq3Rolled = 0
freq4Rolled = 0
freq5Rolled = 0
freq6Rolled = 0

for roll in range (TOTAL_DIE_ROLLS):
    numRolled = randint(1, 6)
    if numRolled == 1:
        freq1Rolled += 1
    elif numRolled == 2:
        freq2Rolled += 1
    elif numRolled == 3:
        freq3Rolled += 1
    elif numRolled == 4:
        freq4Rolled += 1
    elif numRolled == 5:
        freq5Rolled += 1
    else:
        freq6Rolled += 1

print("Frequency 1 rolled: ", freq1Rolled)
print("Frequency 2 rolled: ", freq2Rolled)
print("Frequency 3 rolled: ", freq3Rolled)
print("Frequency 4 rolled: ", freq4Rolled)
print("Frequency 5 rolled: ", freq5Rolled)
print("Frequency 6 rolled: ", freq6Rolled)