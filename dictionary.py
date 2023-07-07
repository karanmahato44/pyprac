student = {
    'name': 'kyto',
    'age': 22,
    'software': ['figma', 'photoshop'],
    'langs': ['python', 'js']
}

# student['phone'] = 987654321
student.update({'name': 'karan', 'phone': '999-999'})

print(student['langs'])
print(student.get('age'))
print(student.get('phone', 'default - not found!'))
print(student)

del student['age']
print(student)

# print(student.pop('name'))

print(student.keys())
print(student.values())
print(student.items())


# imp
print('\n')
for (key, value) in student.items():
    print(f'{key} - {value}')


# dict comprehension
result = {i: i * 2 for i in range(1, 6)}
print(result)
