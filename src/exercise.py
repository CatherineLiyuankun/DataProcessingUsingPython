import math

# Get base
inputOK = False
while not inputOK:
    base = input('Enter base: ')
    if type(base) == type(1.0):
        inputOK = True
    else:
        print('Error.  Base must be floating point number.')

# Get Height
inputOK = False
while not inputOK:
    height = input('Enter height: ')
    if type(height) == type(1.0):
        inputOK = True
    else:
        print('Error.  Height must be floating point number.')

hyp = math.sqrt(base * base + height * height)
print 'Base: ' + str(base) + ',height: ' + str(height) + ', hyp: ' + str(hyp)