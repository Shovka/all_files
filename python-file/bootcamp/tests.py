# my_tuple = ('assasdsa', 'asdsf', 123123, 'asdsa')
# # ozgarmas
# # indexli
# print(my_tuple)
# print(type(my_tuple))
# my_tuple.append(5)


# b = ("dddd",1,2)
# print(b)
# print(type(b))

# print(b[0])
# print(b[-1])
# print(b[1:2])

# a = list(b)
# a[2]= 10
# c = tuple(a)
# print(c)

# task - 1
# tegs = ("abc", "def")

# for i in tegs:
#     print(i[-1])

# task - 2
# a = {2,-3,4,-1}
# for i in a:
#     print(abs(i))

# task - 3
# a = (120,9,9,8,56,1)
# b=set(a)
# c=list(b)
# c.sort()
# print(c)

# task - 4
# a = ('hello', 'salom', 3, 5,'j',5,'j')
# for i in a:
#     if str() == i:
#         result =+ i
#         print(result)

# arr = [1,2,3] # list - array
# list - tartibli elementlae toplami
# tuple - tartibli ozgarmas element toplami
# set - unikal elementlar toplami
# frozenset - unikal ozgarmas elementlar toplami
# dict - kalit orqali murojaat qilinadigan elemrnt toplami
# range - sonlar oraligi

# dict
# d = dict(name="john", age="30")

# d = {"username":"chaplin", "age":40, "skils":["python", "javascript"]}
# print(d)
# print(d.get("username")) #chaplin

# d["salary"] = 500
# d.update({"country":"usa"})
# print(d)

# d = {"username":"chaplin", "age":40, "skils":["python", "javascript"]}

# for elem in d.items():
#     print(elem)

# for k in d.keys():
#     print(k)

# for elem in d.values():
#     print(elem)

# for i in d:
#     print(i)

# d = {"username":"chaplin", "age":40, "skils":["python", "javascript"]}
# d["username"] = "goblin"
# print(d) # {'username': 'goblin', 'age': 40, 'skils': ['python', 'javascript']}

# d.pop("username") # siz korsatgan kalit boyicha elementni ochiradi
# print(d) # {'age': 40, 'skils': ['python', 'javascript']}
# d.popitem() # eng oxirgi elementni ochiradi
# print(d) # {'age': 40}

# task - 1
# alpha = 'abcdef'
# numbers = range(1,7)
# dict1 = {}
# for i in range(6):
#     dict1[alpha[1]]


# task - 2
# d = {"one": 230, "two": "120", "three": "560", "four": "410", "five": "320"}

# def get_user(name,email,password):
#     print(name)
#     print(email)
#     print(password)
#     return True

# get_user("John", "johnDoe", "jhob1234")

# x,y,*z = 1,2,3,4,5, "six", False, [1,2,3]
# print(x,y,z)

# def main(*args):
#     print(args)
#     print(type(args))
#     return len(args)

# print(main(1,2,3,4,5, "six", False, [1,2,3]))


# def daraja(n):
#     return n**2

# def plus(n):
#     return n+2

# a = int(input("a ?"))
# if a%2==0:
#     print(plus(a))
# else:
#     print(daraja(a))

# def user_kwargs(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     if kwargs.get("username") == "chaplin" and kwargs.get("password") == "1234":
#         print('Welcome !')
#         return True
#     else:
#         print("Authition fail !")
#         return False
# user_kwargs(username="chaplin", password="1234", name="John") # welcome !

# def super_func(*args, **kwargs):
#     for i in args:
#         print(i)
#     for k in kwargs.items():
#         print(k)
#     return True
# super_func(1,"some string", False, name="john", age="20")

# print((10>9) * 2 + (10 > 5))
# print(True + 1 - 10 > 5)

# def user_num(*n):
#     return n * 2

# a = input("a ?")
# for i in user_num(a):
#     if i == int(i):
#         print(user_num(a))


# def process_input(user_input):
#     numbers = [int(x) for x in user_input.split(',')]
#     result = []
#     for idx, number in enumerate(numbers):
#         if number % 2 == 0:
#             result.append((chr(ord('a') + idx), number))
#     return sorted(result, key=lambda x: x[1], reverse=True)

# user_input = input("Qiymatlarni kiriting (masalan, a=30, b=50, c=10): ")
# output = process_input(user_input)
# print("Output:", output)

# def pow_num(x):
#     return x**2

# m = map(pow_num, [1,2,3,4,5])
# print(m) 
# print(list(m)) # [1, 4, 9, 16, 25]

# filter  - siz korsatgan ketma-ketlikdagi elementlarni siz ko'rsatgan shartlar boyicha 
# filterlab alohida ketma-ketlik qilib qaytaradi
# arr = [1,21,3,4,5,69,87,5,23,17,3,60,6,4,11,2,3,5,10]
# res = []
# for i in arr:
#     if i > 20:
#         res.append(i)
# print(res)
# def filter_twenty(x):
#     if x > 20:
#         return x

# f = filter(filter_twenty, arr)
# print(f)
# print(list(f))
# print(list(filter(lambda x: x > 20, arr)))

# abc = 'abcdef'
# nums = [1,2,3,4,5,6]
# z = zip(abc,nums)
# print(list(z))

# d = {}
# for k,v in zip(abc,nums):
#     d.update({k:v})
# print(d)


# test_str = "abjsfdk24523fsdsak2342d"
# harflar = list(filter(str.isalpha, test_str))
# numbers = list(filter(str.isdigit, test_str))

# print(f" Harflar: {harflar} \n Sonlar: {numbers}")

# password = "1234"
# username = input("Usernam ? \n")
# user_password = input("password ? \n")

# def is_authention(func):
#     if user_password == password:
#         return func
#     else:
#         return lambda: "Authorization fail !"

# @is_authention
# def login():
#     return f"Welcome back ! {username}"

# @is_authention
# def contact():
#     print("Welcome to contact page !")

# print(login())



# true(50,50) tasks
# a = int(input("a ?"))
# def factorial(n):
#     if n <= 1:
#         return "The end !"
#     else:
#         return n ** n
# print(factorial(a))

# true tasks
# def fak(n,b):
#     if n<=1:
#         return n
#     else:
#         return n*fak(b,n-1)

# print(fak(5,4))

# a = int(input("1 ?"))
# b = int(input("2 ?"))
# c = a,b[-1]

# padez task
# p = int(input('padez ?'))
# q = int(input('qavat ?'))
# s = int(input('kv soni ?'))

# n = int(input('kvartira ?'))

# for i in range(p):
#     for j in range(q):
#         for k in range(1,s+1):
#             if (i*q*s)+j*s+k==n:
#                 print(f'{i+1} padez {j+1} qavat {k}-xonadon')

# a = [1,1,1,2,3,2]
# c = set(a)
# print(c)

# task - 1
# def daraja(n):
#     return n**2

# def plus(n):
#     return n+2

# a = int(input("a ?"))
# if a%2==0:
#     print(plus(a))
# else:
#     print(daraja(a))

# task - 2
# def accert(a):
#     return a*2

# b = (input("Son ? "))
# print(accert(b))

# task - 3

# task - 4
# abc = 'abcdef'
# nums = [1,2,3,4,5,6]
# z = zip(abc,nums)
# print(list(z))

# data strucks
# list, tupe, set, frozenset, dict, range
# l = list() 

# def recursion_func(x):
#     x += 1
#     print(x)
#     if x == 10:
#         print("The end !")
#         return True
#     return recursion_func(x)

# recursion_func(1)

# decorators - oddiy functionni o'zgartiruvchi yoki undan 

a = [-1,2,3]
d = list(map(abs,a))
print(d)