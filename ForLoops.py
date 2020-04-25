for i in range(4):
    print(i)

for i in (0,1,2,3):
    print(i)

#list(range(4))

spam = list(range(0,100,2))
print(spam)

supplies=['pens', 'staplers', 'binders', 'flamethrowers']
for i in range(len(supplies)):
   print('Index'+ str(i) + ' in supplies is: ' + supplies[i])

supplies = ['pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens']
print(len(supplies))

for i in range(len(supplies)):
   print('Index'+ str(i) + ' in supplies is: ' + supplies[i])

cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

size, color, disposition = cat

a = 'aaa'
b = 'bbb'
a,b=b,a
print(a)

spam = 42
spam = spam + 1
spam += 1 #Does the same as spam = spam + 1



