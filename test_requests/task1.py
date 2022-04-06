import os
import requests

txt = os.path.join('.', 'dirname', 'dataset_3378_2.txt')
filename2 = 'result.txt'


def read_file(file):
    with open(file) as inf:
        s = inf.readline()
        return s


def write_result(file, i):
    with open(file, 'w') as res:
        res.write(str(i))


def requset_input(url1):
    r = requests.get(url1, stream=True)
    content = str(r.text).splitlines()
    return content


def count(text1):
    i = 0
    for s in text1:
        print(s)
        i += 1
    print(i)
    return i


url = read_file(txt)
text = requset_input(url)
count_of_stroke = count(text)
write_result(filename2, count_of_stroke)




