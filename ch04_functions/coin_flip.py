'''
simulate flipping a coin multiple times
count the number of times each side landed face-up
'''

from random import randrange

NUM_COIN_FLIPS = 20    # total number of coin flips

for flip in range(NUM_COIN_FLIPS):
    coinFace = randrange(2)   # simulates flipping a coin; 0 = H, 1 = T
    
    if coinFace == 0:
        print("H", end=' ')
    else:
        print("T", end=' ')