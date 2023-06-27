import os
import datetime


print(os.getcwd())
# os.chdir('/Users/kyto/Desktop')
print(os.getcwd())
print(os.listdir())

# os.mkdir('foo')
# os.makedirs('foo/bar')
# os.rmdir('foo')
# os.removedirs('foo/bar')

# os.rename('dict.py', 'dictionary.py')

mod_time = os.stat('main.py').st_mtime
print(datetime.datetime.fromtimestamp(mod_time))


homedir = os.environ.get('HOME')
print(homedir)


path = os.path.join(os.environ.get('HOME'), 'test.txt') # imp
print(path)


print(os.path.exists('/tmp/foo'))
print(os.path.isdir('/tmp/'))
print(os.path.isfile('/tmp/'))
print(os.path.splitext('/tmp/foo.txt'))