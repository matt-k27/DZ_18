import random

print('DZ18')


def rand_list(number):
    randomList = []
    for i in range(random.randint(5, 20)):
        temp = random.randint(number, 100)
        if temp % number:
            temp -= temp % number
        randomList.append(temp)
    return randomList


def common_elements():
    randSet5 = set(rand_list(5))
    randSet3 = set(rand_list(3))
    result = {"randSet5": randSet5, "randSet3": randSet3, "resIntersection": randSet5.intersection(randSet3)}
    return result


print(common_elements())

print('Thank you for using')
