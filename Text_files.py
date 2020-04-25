helloFile = open('C:\\Users\koenl\Dropbox\Documents\Coding\Python\hello.txt')
print(helloFile.read())
helloFile.close()
helloFile = open('C:\\Users\koenl\Dropbox\Documents\Coding\Python\hello.txt')
content = helloFile.read()
print(content)

helloFile.close()
helloFile = open('C:\\Users\koenl\Dropbox\Documents\Coding\Python\hello.txt', 'w') #'w' overwrites everything. 'a' appends and adds to the file
helloFile.write('Hello!!!!!!!!')
helloFile.write('Hello!!!!!!!!')
helloFile.write('Hello!!!!!!!!')
helloFile.close()

baconFile = open('bacon.txt', 'a') # appends and adds to existing file instead of erasing
baconFile.write('bacon is not a vegetable')

baconFile.close()

import os
print(os.getcwd())

import shelve
shelFile = shelve.open('mydata') #shelFile files are very similar to dictionaries
shelFile['Cats'] = ['Zophie', 'Pooka', 'Fat-tail', 'Cleo']
shelFile.close()

shelFile = shelve.open('mydata') #creates 3 files. mydata.dir, mydata.dat, mydata.bak
print(shelFile['Cats'])


