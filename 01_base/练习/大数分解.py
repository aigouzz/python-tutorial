'''每个数字可以写成多个质数的乘积，给定一个数字，请你分解为多个质数'''

def fun(num, list=None):
    if list is None:
        list = []
    for i in range(2, num):
        while num % i == 0:
            list.append(i)
            num = int(num / i)
            if num > 1:
                fun(num)
    return list
x = 9*5
print(fun(x))

def divis(num, list=None):
    if list is None:
        list = []
    if (num == 1):
        return [1]
    for i in range(2, num):
        if num % i == 0:
            list.append(i)
            num = int(num / i)
            if num > 1:
                divis(num)
    return list

a1 = 88 * 45
print(divis(a1), 'a1')
