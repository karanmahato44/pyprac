import sys

result = (x * 2 for x in range(1, 101))
print('size =', sys.getsizeof(result))
for i in result:
    print(i)
