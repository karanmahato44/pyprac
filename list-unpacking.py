# first, second, third, *others = [1, 2, 3, 4, 5, 6, 10, 100, 10000]
first, *others, last = [1, 2, 3, 4, 5, 6, 10, 100, 10000]
print(first, others, last)


# tuple unpacking
letters = ['a', 'b', 'c', 'd', 'e']

for index, letter in enumerate(letters):  # unpacked here in index, letter
    print(index, letter)
