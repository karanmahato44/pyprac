from array import array

nums = array('i', [1, 2, 3])

nums.append(44)
nums.append(10)
nums.insert(0, 20)
nums.pop()

for i in nums:
    print(i)
