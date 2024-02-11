# a = 'text lorem3 i4psum572'
# x = [int(x) for x in a if x.isdigit()]
# def func(*args):
#     for i in args:
#         if i == sorted(i):
#             return True
#         else:
#             return False
# print(func(x))


# a = [3, 2]
# def oshish_tartibi(a):
#     n = len(a)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]

# oshish_tartibi(a)

# arr0bj = [
#     {
#         "data":[[1,2,3],[4,5,6],[7,8,9]],
#     },
#         {
#         "data":[[1,2,3],[4,5,6],[7,8,9]],
#     },
#         {
#         "data":[[1,2,3],[4,5,6],[7,8,9]],
#     }
# ]
# result = 0

# for i in arr0bj:
#     for j in i['data']:
#         result += sum(j)
# print(result)

# from random import randint
# a = int(input("Son kiriting: "))
# b = int(input("2nchi son"))
# s = []
# for i in range(1,6):
#     a = randint(a,b)
#     s.append(a)
# print(f'Tasodifiy 5-ta son: {s}')

# a = [2,1,5,3]
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         print(j)
#         if a[j] < a[i]:
#             a[i], a[j] = a[j], a[i]
# print(a)

# def _sort(array):
#     less = []
#     equal = []
#     greater = []

#     if len(array)>1:
#         privot = array[0]
#         for x in array:
#             if x < privot:
#                 less.append(x)
#             elif x==privot:
#                 equal.append(x)
#             elif x > privot:
#                 greater.append(x)
#         return _sort(less) + equal + _sort(greater)
#     else:
#         return array
# print(_sort([6,3,2,6,1,3,5]))

