# with open('test.txt', 'r') as f:
# content = f.readline()
# content = f.readlines()
# content = f.read()

# for line in f:
#   print(line, end='')

# size_to_read = 10

# content = f.read(size_to_read)
# print(content)
# print(f.tell())

# f.seek(40)
# content = f.read(size_to_read)
# print(content)
# print(f.tell())

# while (len(content) > 0):
#   print(content, end='*')
#   content = f.read(size_to_read)


with open('test.txt', 'r') as fr:  # for images open in binary mode => with open('file.png', 'rb')
    with open('test2.txt', 'w') as fw:
        for line in fr:
            fw.write(line)
