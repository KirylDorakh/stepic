import os
os.path.join('.', 'dirname', 'filename.txt')

inf = open('file.txt', 'r')
#  чтение одной строки
s1 = inf.readline()
s2 = inf.readline()
print(s1, end='')
print(s2)
inf.close()

with open('file.txt') as inf:
    s1 = inf.readline()
    s2 = inf.readline().strip()
    print(s1)
    print(s2)


with open('file.txt') as inf:
    for line in inf:
        line = line.strip()
        print(line)
