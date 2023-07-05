nums = [1, 2, 3, 4, -1, -2, -44, 100]


def foo(data): return data * data


result = map(foo, nums)
print(list(result))
