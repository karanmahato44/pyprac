from functools import reduce

nums = [5, 4, 3, 2, 1]
def foo(x, y): return x * y


result = reduce(foo, nums)

print('result is:', result)
