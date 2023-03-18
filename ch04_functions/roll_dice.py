'''
simulate rolling a die multiple times
count the number of times each side was rolled
'''

from random import randrange

NUM_ROLLS = 6_000_000    # total number of dice rolls

# resets the frequency counter for each die face to 0
face1_freq = 0
face2_freq = 0
face3_freq = 0
face4_freq = 0
face5_freq = 0
face6_freq = 0

for diceRoll in range(NUM_ROLLS):
    diceFace = randrange(1,7)
    if diceFace == 1:
        face1_freq += 1
    elif diceFace == 2:
        face2_freq += 1
    elif diceFace == 3:
        face3_freq += 1
    elif diceFace == 4:
        face4_freq += 1
    elif diceFace == 5:
        face5_freq += 1
    else:
        face6_freq += 1

print(f'Face{"Frequency":>13}')
print(f'{1:>4}{face1_freq:>13}')
print(f'{2:>4}{face2_freq:>13}')
print(f'{3:>4}{face3_freq:>13}')
print(f'{4:>4}{face4_freq:>13}')
print(f'{5:>4}{face5_freq:>13}')
print(f'{6:>4}{face6_freq:>13}')