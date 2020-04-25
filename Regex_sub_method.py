import re
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent alice gave the secret documents to Agent bob'))
print(namesRegex.sub('REDACTED','Agent Alice gave the secret documents to Agent Bob'))

namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob'))
print(namesRegex.sub(r'Agent \1*****','Agent alice gave the secret documents to Agent bob'))

re.compile(r'''
\d\d\d 		# area code
-      		# first dash
\d\d\d 		# first 3 digits
-      		# second dash
\d\d\d\d 	#last 4 digits
\sx\d{2,4} #extension like 1234''', re.IGNORECASE | re.DOTALL | re.VERBOSE) # re.VERBOSE ignores whitespaces, makes it more readable
#combine multiple arguments with | bitwise operator
