message = 'hey!'
name = 'kyto'
new_message = message.replace('hey!', 'namaste')

print(message.lower())
print(message.upper())

print(message.count('Hell'))
print(message.find('nice'))
print(new_message)

print(f'{message} { name.upper() }, welcome') # can user exp. inside {} too
# print(dir(name)) # see all availabe att. and methods of given type
print(help(str.upper))

