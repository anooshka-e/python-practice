'''
simulating the game "craps"
 game rules:
    - roll two six sided dice
    - add the numbers rolled
    - if the sum is 7 or 11, player wins
    - if the sum is 2, 3, or 12, player loses
    - if the sum is any other number (4, 5, 6, 8, 9, or 10) that number becomes player's point
    - if player gains a point, they must reroll until they get the same point to win
    - if the player rolls a 7 before their second point, the player loses
'''

from random import randint

def rollDice():
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    return (die1, die2)             # returning die1 and die2 as a tuple

def showDice(dice):
    firstDie, secondDie = dice      # unpacking of a tuple
    print("(Die 1, Die 2) = (%d, %d)" %(firstDie, secondDie))
    print("Sum of dice =", sum(dice))

diceValues = rollDice()
showDice(diceValues)

# calculate sum of dice, determine the game status (won/lost/continue), and points based on first roll
sumOfDice = sum(diceValues)

if sumOfDice in (7, 11):            # same as ((sumOfDice == 7) or (sumOfDice == 1))
    gameStatus = "WON"
elif sumOfDice in (2, 3, 12):
    gameStatus = "LOST"
else:
    gameStatus = "CONTINUE"
    gamePoint = sumOfDice
    print("Game point is %d, please roll again." %gamePoint)

'''
as long as gameStatus is CONTINUE
 - roll dice
 - display each die value
 - calculate sumOfDice
 - if sumOfDice is same as gamePoint,set gameStatus to WON
 - if sumOfDice is equal to 7, set gameStatus to LOST
 - otherwise, continue
'''

while(gameStatus == "CONTINUE"):
    diceValues = rollDice()
    showDice(diceValues)
    sumOfDice = sum(diceValues)
    if(sumOfDice == gamePoint):
        gameStatus = "WON"
    elif(sumOfDice == 7):
        gameStatus = "LOST"
    else:
        gameStatus = "CONTINUE"

'''
print whether the player won or lost based on game status
'''

if(gameStatus == "WON"):
    print("Congratulations, you win!")
else:
    print("You lost.")