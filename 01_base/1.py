a1 = 'abcdefghijklmn'
a2 = list()
a2 = [1,2,3,4,5,6,7,8,9,10]
a3 = a2[::-1]
a4 = [1,2,3,4,5]
a4.reverse()
a5 = [1,1,1,1]
a5.extend([2,2,2])
# print(a5)
a6 = tuple(a5)
# print(a6, type(a6), a6.index(1), a6.count(1))
a7 = [a5, a4]
a8 = a7[:]
a8[0][0] = 100
print(a5, a6, a7, a8, a7 == a8, a7 is a8, set(a5))