'''
practice using "while" loops
'''

# x = 0
# while (x <= 20):
#     x += 1
#     if(x == 5):
#         continue
#     if(x == 13):
#         break
#     print(x)

total = 0
gradeCounter = 0

grade = float(input("Enter a grade, enter -1 to exit: "))

while(grade != -1.0):
    total += grade
    gradeCounter += 1
    grade = float(input("Enter a grade, enter -1 to exit: "))

if(gradeCounter != 0):
    average = (total / gradeCounter)
    print("The average is %.2f." %average)
else:
    print("No grades entered, average can not be calculated.")