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
    die1 = randint(1,6)
    die2 = randint(1,6)

    return (die1, die2)

def diceSum(diceRoll):
    die1, die2 = diceRoll      # unpacks the tuple
    diceTotal = die1 + die2    # sum of both dice: the number the player rolled
    print("You rolled", die1, "and", die2, "to score", diceTotal, "points.")

    return diceTotal

dicePair = rollDice()
sumOfDice = diceSum(dicePair)

'''
determine if player wins, loses, or continues
based on first roll

7 or 11  = win
2, 3, 12 = lose
other    = continue
'''
if sumOfDice in (7, 11):       # player wins and the game ends
    gameStatus = "WIN"
elif diceSum in (2, 3, 12):    # player loses and the game ends
    gameStatus = "LOSE"
else:                          # the game doesn't end and player continues
    gameStatus = "CONTINUE"
    pointValue = sumOfDice
    
    print("You earned", pointValue, "points. You must roll until you get the same number to win.")

'''
determine if player wins, loses, or continues
based on number of points scored in first roll
'''
while gameStatus == "CONTINUE":
    diceValue = rollDice()     # rerolls the dice as long as the game continues
    pointsScored = diceSum(diceValue)

    if pointsScored == pointValue:
        gameStatus = "WIN"       # player rerolls their number and wins
    elif pointsScored == 7:
        gameStatus = "LOSE"      # player rolls 7 and loses
    else:
        gameStatus = "CONTINUE"  # player rolls a different number and continues

if gameStatus == "WIN":
    print("Congratulations, you win!")
else:
    print("You lost. Better luck next time.")