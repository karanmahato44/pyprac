import os

os.chdir('/Users/kyto/code/python/pythonOOP/testdir')
print(os.getcwd())

# print(os.listdir())

for f in os.listdir():
    filename, extension = os.path.splitext(f)
    planet, series, ep = filename.split('- ')
    ep = ep.strip()[1:].zfill(4)
    
    new_name = f'{ep} {planet} {extension}'
    os.rename(f, new_name)