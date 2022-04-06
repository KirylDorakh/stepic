def f(i):
    i += 1
    return i


def list_work(rangenum, numbers, d):
    for num in range(rangenum):
        numbers.append(int(input()))
    for number in numbers:
        if number in d.keys():
            d[number] += 1
        else:
            d[number] = 1


n = int(input())
list1 = list()
dict1 = {}
dict2 = {}

list_work(n, list1, dict1)

for number in list1:
    if dict1[number] == 1:
        x = number
        v = f(x)
        print(v)
    else:
        if number in dict2.keys():
            print(dict2[number])
        else:
            x = number
            v = f(x)
            print(v)
            dict2[number] = v
