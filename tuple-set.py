# tuples immmutable

names = ('karan', 'kyto', 'foo', 'bar')
# names[2] = 'qux'
print(names)


# sets

names = {'karan', 'kyto', 'foo', 'bar'}  # will appear in any random order
nums = {1, 2, 3, 4, 5, 'foo'}

# sets are optimized for testing if present or absent
print('karan' in names)

print(names.union(nums))  # same as names | nums
print(names.intersection(nums))  # names & nums
print(names.difference(nums))  # names ^ nums
