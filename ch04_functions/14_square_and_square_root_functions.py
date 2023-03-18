'''
 - create a function to calculate the square of an input
 - create a function to calculate the square root of an input
'''
def calcSquare(x):
    return (x ** 2)
    # print("The square of %.2f is %.2f." %(x, x ** 2))

def calcSquareRoot(y):
    return (y ** (1 / 2))

# x = square(10)
num1 = float(input("Enter a number to be squared: "))
print("The square of %.2f is %.2f." %(num1, calcSquare(num1)))

num2 = float(input("Enter a number to be square rooted: "))
print("The square root of %.2f is %.2f." %(num2, calcSquareRoot(num2)))