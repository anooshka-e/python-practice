'''
input a grade as a float
letter grade as the output
'''

grade = float(input("Enter your grade: "))

if(grade >= 90):
    print("You have an A.")
elif(grade >= 80):
    print("You have a B.")
elif(grade >= 70):
    print("You have a C.")
elif(grade >= 65):
    print("You have a D.")
else:
    print("You have an F.")