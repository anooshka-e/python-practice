'''
practice using functions and assigning values to them
'''

from math import *

def circleArea (radius):
    area = (pi * radius ** 2)
    print ("The area of the circle is %.4f." %(area))

r = float(input("Please enter the radius of circle 1: "))
circleArea (r)
r = float(input("Please enter the radius of circle 2:"))
circleArea (r)