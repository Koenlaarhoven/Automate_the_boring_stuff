def isPhoneNumber(text): #415-555-1234
    if len(text) != 12:
        return False #not phone number sized
    for i in range(0,3):
        if not text[i].isdecimal():
            return False #no area code
    if text[3] != '-':
            return False #miss ing dash
    for i in range (4,7):
            if not text[i].isdecimal():
                return False # no first 3 digits
    if text[7] != '-': 
                return False #missing second dash
    for i in range(8,12):
                if not text[i].isdecimal():
                    return False #missing last 4 digits
    return True

print(isPhoneNumber('415-555-1234'))
print(isPhoneNumber('hello'))

message = 'call me 415-555-1011 tomorrow, or at 415-444-9999 for my office line'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone number')


import re
message = 'call me 415-555-1011 tomorrow, or at 415-444-9999 for my office line'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group())

