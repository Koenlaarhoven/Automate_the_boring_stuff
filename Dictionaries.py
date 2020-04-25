myCat={'size':'fat', 'color':'gray', 'disposition':'loud'}
print(myCat['size'])

'My cat has ' +myCat['color'] + 'fur.'

spam={12345:'Luggage combination', 42:'The answer'}
print([1,2,3]==[3,2,1])

eggs={'name':'sophie','species':'cat', 'age':8}
ham={'species':'cat','name':'sophie','age':8}
print(ham==eggs)


print(list(eggs.keys()))
list(eggs.values())
list(eggs.items())

for k in eggs.keys():
      print(k)

for v in eggs.values():
    print(v)

for k,v in eggs.items():
    print(k,v)

print('cat' in eggs.values())

if 'color' in eggs:
    print(eggs['color'])

picnicitems={'apples':5, 'cups':2}
print('I am bringing ' + str(picnicitems.get('napkins',0))+' to the picnic')

eggs.setdefault('color','black')

print('NEW PROGRAM')
message='It was a bright cold day in april, and the clocks were striking thirteen.'
count={} #'r'=12

import pprint
for character in message.upper():
      count.setdefault(character,0)
      count[character]=count[character]+1
pprint.pprint(count)
#print(count)
