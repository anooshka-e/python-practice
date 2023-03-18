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

pseudocode
 step 1:
    - roll two dice using randint
    - add numbers and store it in a variable
step 2:
    - check if the player won
    - check if the house won
    - check if the player gained points
step 3:
if player gained points:
    - reroll dice
    - check if the player won
    - check if the player lost
    - check if the player did neither and roll again
'''
from random import randint

def diceRoll():
    die1 = randint(1, 6)
    print("Die 1 rolled a", die1)
    die2 = randint(1,6)
    print("Die 2 rolled a", die2)
    diceSum = die1 + die2
    return diceSum

sum = diceRoll()
rollCount = 1

print("The sum of the dice is", sum)

if((sum == 7) or (sum == 11)):
    gameStatus = "WON"
    print("Player won with a",  sum)
elif((sum == 2) or (sum == 3) or (sum == 12)):
    gameStatus = "LOST"
    print("Player lost with a", sum)
else:
    print("Player made %d points. You must reroll to make the same points to win the game." %sum)
    gameStatus = "CONTINUE"
    pointMade = sum

while(gameStatus == "CONTINUE"):
    totalOfDice = diceRoll()
    rollCount += 1
    if(totalOfDice == pointMade):
        gameStatus = "WON"
        print("Player won with two matching %d's." %pointMade)
    elif(totalOfDice == 7):
        gameStatus = "LOST"
        print("Player lost.")
    else:
        gameStatus = "CONTINUE"
        print("You rolled a %d. Roll again." %totalOfDice)

print("You rolled %d times." %rollCount)