import os
import requests

filename = os.path.join('.', 'dirname', 'dataset_3378_2.txt')


def read_file(file):
    with open(file) as inf:
        s = inf.readline()
    return s


url = read_file(filename)
print(url)

while True:
    if requests.get(url).text[0:2] == 'We':
        print(requests.get(url).text)
        break
    else:
        link = requests.get(url).text
        print(link)
        while True:
            if url[-1] == '/':
                break
            else:
                url = url[0:-2]
        url = url + link
        print(url)
