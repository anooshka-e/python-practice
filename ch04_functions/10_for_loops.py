'''
practice using "for" loops

for x in range (20):              x is assigned the value of 0, x increases by 1 until it reaches 20 (prints 0 - 19)

loop control statements:
    - break: exits out of the loop immediately
    - continue: skips the iteration
'''

# for x in range (20):        prints range up to 20
#    print(x)                 prints 0 - 19
#    print(x + 1)             prints 0 - 20

for x in range (55, 100):
    if(x == 57):
        continue
    if(x == 60):
        break
    print(x)