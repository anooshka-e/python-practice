'''
create a list of integers
list contains values of any datatypes, can be a mix of strings, integers, floats, booleans, etc.
lists conatianed in []
print the sum of the integers in the array
'''

total = 0

for x in [-50, 48, 0, 15, -24]:
    total = (x + total)          # same as (total += x)

print("Total = ", total)