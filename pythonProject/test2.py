def word_count(words):
    d = {}
    for word in words:
        if word in d.keys():
            d[word] += 1
        else:
            d[word] = 1
    return d


def make_low(list):
    low = []
    for word in list:
        low.append(word.lower())
    return low


a = input().split()
b = make_low(a)

res = word_count(b)

for key, value in res.items():
    print(key, value)

