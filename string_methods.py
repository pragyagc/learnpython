msg='hello python'

# calculate no of strings
print(len(msg))

#convert to uppercase
print(msg.upper())

#finding index  of strings
print(msg.find('p'))
print(msg.find('1'))

#replacing certain words or letter
print(msg.replace('python','world'))
print(msg.replace('p','g'))

#boolean function to check whether the word is in the string or not
print('Python'in  msg)
print('python'in  msg)
print('n'in  msg)