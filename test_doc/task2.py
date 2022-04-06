import os
file = os.path.join('.', 'dirname', 'dataset_3363_33.txt')

list1 = []
dict1 = {}
dict2 = {}

with open(file) as inf:
    while True:
        s = inf.readline()
        if s == '':
            break
        else:
            list1.append(s.lower().split())

for i in list1:
    for word in i:
        if word in dict1:
            dict1[word] += 1
        else:
            dict1[word] = 1

for key, value in dict1.items():
    if not dict2:
        dict2[key] = value
    if dict2:
        for result, count in dict2.items():
            if count == value:
                print(key, value)
                print('count == value')
                print(f'{key}, {result}, {key < result}')
                if key < result:
                    dict2.clear()
                    dict2[key] = value
                    print('dict2', dict2)
            if count < value:
                dict2.clear()
                dict2[key] = value


for key, value in dict2.items():
    result = str(key) + " " + str(value)
print(result)

with open(file, 'w') as out:
    out.write(result)
