'''
Takes a number from the user and prints all numbers from 0 to the inputted number
Indicates whether each number is odd or even
'''

# prompt the user, accept a number, and store it into a variable
num = int(input("Enter an integer: "))
#print(num)

# loop through num and print 0 - num
# check if even
for x in range (num + 1):
    if((x % 2) == 0):
        print(x, "=> even")
    else:
        print(x, "=> odd")