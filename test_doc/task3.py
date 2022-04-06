import os
file = os.path.join('.', 'dirname', 'dataset_3363_4.txt')

list1 = []


def read_file(list2):
    with open(file) as inf:
        while True:
            s = inf.readline()
            if s == '':
                break
            else:
                list2.append(s.split(';'))


def gpa(list2):
    gpaball = []
    for pupil in list2:
        pupil.pop(0)
        print((int(pupil[0]) + int(pupil[1]) + int(pupil[2])) / 3)
        gpaball.append((int(pupil[0]) + int(pupil[1]) + int(pupil[2])) / 3)
    return gpaball


def subjects(list2):
    i = 0
    math = 0
    science = 0
    language = 0
    result1 = []
    for pupil in list2:
        math = math + int(pupil[0])
        science = science + int(pupil[1])
        language = language + int(pupil[2])
        i += 1
    result1.append(math/i)
    result1.append(science/i)
    result1.append(language/i)
    print(i)
    result = str(result1[0]) + ' ' + str(result1[1]) + ' ' + str(result1[2])
    return result

def write_file(result):
    with open(file, 'w') as out:
        for line in result:
            out.write(str(line)+'\n')


read_file(list1)
ball = gpa(list1)
sub = subjects(list1)
ball.append(sub)
write_file(ball)
