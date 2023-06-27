langs = ['python', 'javascript', 'shell', 'java']
tools = ['git', 'figma']
nums = [1, 2, 3, 4, 5]


langs.append('c/c++')
print(langs)

langs.insert(2, 'go')
langs.extend(tools)
print(langs)

langs.remove('java')
print(langs)
langs.pop()
print(langs)

# list reversing
reversed = []
for i in range(len(langs) - 1, -1, -1):
    reversed.append(langs[i])

print(reversed)
print(langs[::-1])

nums.reverse() # modifies the og list
print(nums)


# sorting
langs.sort() # asc            sort() method, modifies og 
print(langs)
langs.sort(reverse=True) # dec
print(langs)

print(sorted(nums))          # sort fn, returns new list
print(sorted(nums, reverse=True))
print(min(nums))
print(max(nums))
print(sum(nums))

print(langs.index('javascript'))
print('python' in langs)
print('python' not in langs)