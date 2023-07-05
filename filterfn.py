nums = [1, 2, 3, 4, -1, -2, -44, 100]


def foo(data): return data >= 0 or data == -44


result = filter(foo, nums)

print(list(result))
