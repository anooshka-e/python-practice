'''
write a function to multiply all numbers in a tuple / list
'''

def getProduct(*args):
    product = 1
    for i in args:
        product *= i
    print(product)

grades = (2, 9, 8, 7, 6)
getProduct(*grades)

gpa = [4, 3, 2, 1]
getProduct(*gpa)

ages = (3, 4, 1, 5, 0)
getProduct(*ages)

gamePoints = (-2, 8, 5.7, -2)
getProduct(*gamePoints)