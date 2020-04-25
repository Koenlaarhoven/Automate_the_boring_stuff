#raise Exception('This is the error message')



'''

**********
*        *
*        *
*        *
**********

'''

def boxPrint(symbol, width, height):
    print(symbol * width)

    for i in range(height-2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

boxPrint('*', 15, 5,)
boxPrint('O', 5, 16,)
boxPrint('**', 15, 5,) #This is a bug, not working as intended

def boxPrint(symbol, width, height):
    if len(symbol) !=1:
        raise Exception('"symbol" needs to be a single character string')
    if (width < 2) or (height < 2):
            raise Exception('"width" and "height" must be greater or equal to 2')
    
    print(symbol * width)

    for i in range(height-2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

boxPrint('*', 15, 5,) #It is now impossible to input ** or a width and height less than 2

import traceback
try:
    raise Exception('This is the error message')
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written in error_log.txt')

import os
print(os.getcwd)

assert False, 'This is the error message.'
