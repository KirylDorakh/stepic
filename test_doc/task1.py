import os
file = os.path.join('.', 'dirname', 'dataset_3363_2-2.txt')

with open(file) as inf:
    s1 = inf.readline()

list1 = []
list2 = []
s2 = ''
s3 = '0'
count = 0
result = ''
print(range(0, len(s1)))
print(s2*int(s3))
for i in s1:
    list1.append(i)

count = 0

while True:
    if list1[count] == '\n':
        list2.append(s2 * int(s3))
        print(f'list1 = {list1}, s2 = {s2}, s3 = {s3}, list2 = {list2}')
        break
    elif list1[count].isalpha():
        list2.append(s2*int(s3))
        s2 = list1[count]
        s3 = ''
        print(s2)
        list1.remove(list1[count])
        print(f'list1 = {list1}, s2 = {s2}, s3 = {s3}, list2 = {list2}')
    elif list1[count].isdigit():
        s3 = s3 + list1[count]
        list1.remove(list1[count])

for i in list2:
    result = result + i

with open(file, 'w') as out:
    out.write(result)
