def greet(fname, lname='xxxxxxx'):
    return f'hi! {fname} {lname}'


print(greet('karan', lname='mahato'))
print(greet('karan'))


# args and kwargs

def student_info(*args, **kwargs):
    print(args)  # args is a tuple
    print(kwargs)  # kwargs is a dict


student_info('compsci', 'math', 'python', name='kyto', age=22, foo='bar')

subjects = ['art', 'account', 'js']
info = {
    'name': 'karan',
    'age': 44,
    'lorem': 'ipsum'
}

# student_info(subjects, info) # will just be passed as positional args

# will be unpacked and passed as *args & **kwargs
student_info(*subjects, **info)
