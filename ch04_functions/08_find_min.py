'''
input three integers
use "if-elis-else" statements to find the minimum
'''

num1 = int(input("Enter intger 1: "))
num2 = int(input("Enter integer 2: "))
num3 = int(input("Enter integer 3: "))
minimum = num1

if (minimum > num2):
    minimum = num2
if (minimum > num3):
    minimum = num3

print("The minimum number is ", minimum)