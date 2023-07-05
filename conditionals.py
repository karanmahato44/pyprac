lang = 'java'

if lang == 'Python':
    print('py')
elif lang == 'JavaScript':
    print('js')
else:
    print('no lang')


user = 'admin'
logged_in = False

if user == 'admin' and not logged_in:
    print('admin page')
else:
    print('invalid creds.')


a = [1, 2, 3]
b = [1, 2, 3]

c = a

print(id(a))
print(id(b))
print(id(c))

print(a == b)  # compares values
print(a is b)  # compares objects/references of c, js/they are diff obj in memory
print(c is a)
