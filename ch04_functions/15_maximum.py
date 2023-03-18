'''
Calculate the maximum number out of three values
'''

def getMaximum(num1, num2, num3):
    maximum = num1
    if(num2 > maximum):
        maximum = num2
    if(num3 > maximum):
        maximum = num3
    
    return maximum

x = getMaximum(8, 40, 7)
print(x)

y = getMaximum(90, -68, 29)
print(y)

z = getMaximum(22.4, 66.6, 42.01)
print(z)

letter = getMaximum('a', 'g', 'b')
print(letter)

color = getMaximum("green", "blue", "red")
print(color)