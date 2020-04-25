def spam():
    global eggs #Tells python to call upon the global variable instead of the local variable
    eggs=99 #local variable overrules the global variable
    print(eggs)

eggs=42 #if no local variable is assigned Python will call upon this global variable
spam()
print(eggs)
