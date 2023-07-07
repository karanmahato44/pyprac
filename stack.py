tabs = []

tabs.append('yt')
print(tabs)
tabs.append('linkedin')
tabs.append('github')
tabs.append('reddit')
print(tabs)
tabs.pop()
print(tabs)

print('stack top =', tabs[-1])

if not tabs:
    print('back button disabled')
