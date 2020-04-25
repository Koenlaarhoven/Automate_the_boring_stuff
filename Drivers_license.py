name = 'Koen'
agents = 6
others = 'John Arie Bas Zoloe'

allnames = name + ' ' + others
words = allnames.split()
words.sort()

for word in words:
    print(word)

print(words.index(name))
time = words.index(name) * 20
print(time)