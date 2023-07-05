def foo(num):
    if (num % 3 == 0) and (num % 5 == 0):
        return 'fizbuzz'
    if (num % 3 == 0):
        return 'fizz'
    if (num % 5 == 0):
        return 'buzz'
    return num


for num in range(1, 101):
    print(foo(num))
