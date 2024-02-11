import datetime
import random
import math

# user_date = input("YYYY/MM/DD")

# def get_user_age(user_birthday):
#     today = datetime.datetime.now()
#     user_age = today.year - int(user_birthday.split("/"[0]))
#     return user_age
# print(get_user_age(user_date))

# number = input("Tel raqamingiz: (xx-xxx-xx-xx): ")

# def show_phone_number_result(phone_number):
#     a = number.split("-")
#     c = a[2:]
#     c = [int(x) for x in c]
#     return sum(c)

# print(show_phone_number_result(number))
# import random
# def randomnum_plus():
#     s = 0
#     for i in range(1,6):
#         a = random.randint(1, 30)
#         print(a)
#         s += a
#     return s
# print(randomnum_plus())

# args , kwargs
# def summa(*nums):
#     print(nums) # (1, 2, 3, 4, 5)
#     amount = 0
#     for i in nums:
#         amount += i
#     return amount

# print(summa(1,2,3,4,5)) # 15

# def kwars_summa(**kwargs):
#     print(kwargs) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#     amount = 0
#     for i in kwargs.values():
#         amount += i
#     return amount

# print(kwars_summa(a=1,b=2,c=3,d=4,e=5)) # 15


# def super_func(*args, **kwargs):
#     print(args) # (1, 2)
#     print(kwargs) #  {'number1': 3, 'number': 2}


# super_func(1,2,number1=3, number=2)

# anonim function
# summa = lambda x: x+1
# print(summa(1)) # 2


# def main(x):
#     if x>10:
#         s = lambda num: num ** 2
#         return s(x)
#     else:
#         return x + 2
# print(main(x=2)) # 4
# print(main(x=15)) # 225

# arr = list(range(1,30,3))
# print(arr) # [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]

# zip(), filter(), map()

# arr = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
# version 2
# print([x for x in arr if x %2==1]) # [1, 7, 13, 19, 25]
# version 3
# print(list(filter(lambda x: x%2==1, arr))) # [1, 7, 13, 19, 25]

# filter - alohida funksiya qabul qiladi va ketma-ketlikdagi barcha elementni shu funksiyaga qarab filterlaydi
# misol:
# print(list(filter(lambda num: num>4, [1,2,3,4,5,6,7,8,9,10]))) # [5, 6, 7, 8, 9, 10]

# task - 1
# d = {'a':1, 'b':234, 'c':555, 'd':15}
# print(list(filter(lambda x: x[1]>20, d.items())))


# task - 2
# a = """
# Ikka5lasida ham 2 tadan task bo'ladi. Akademik IELTS ning birinchi topshirig'ida o'sha
# ko'pchilik yoqtirmaydigan diagrammalarni rasmiy tilda tasvirlash12 yoki kerak bo'lsa 
# Generel'da letter yani ma'lum bir turdagi xat yozish
# kerak bo'ladi. U xat esa norasmiy tilda bo'lishi ham mumkin.
# """
# print(sum(int(x) for x in a if x.isdigit()))


# task - 3
# a = input('Telefon raqam kiriting Misol; 997776655: ')
# print(f'{a[:2]}-{a[2:5]}-{a[5:7]}-{a[7:]}' if len(a) == 9 else 'Misol keltirgandaqa qilish kerak edi')

# zip - berilgan

# map - Berilgan ketma-ketlik elementlari berilgan funksiyani qollaydi
# lorem = 'lorem ipsum dolor amet'
# print(list(map(lambda x: x.upper(), lorem.split(" "))))

# s = []
# a = """
# An asterisk pyramid may not be the most useful example, but it surely tests your 
# understanding of loops and maths in Python.
# To create a pyramid, you need to start with 1 asterisk. On the next 
# line you have 3, then 5,7, and so on. In other words, the number of asterisks is 2*i + 1, 
# where i is the row number (or the height) of the pyramid.
# Now you got the number of asterisks.
# Then you need to know how many spaces you need to the 
# left of the asterisks to make it look like a pyramid.
# In the first row, the number of spaces is the same as 
# the height of the pyramid. Then on the second row, it is one less. On the third one less again. So you need to add one less space for each row of asterisks. In other words, the number
# of spaces is h-i-1, where h is the pyramid height and i is the row number.
# """
# def salom(*args):
#     return args[-2:]
# print(salom(1,2,3,4,5))

# def alik(*kwargs):
#     if kwargs.values() > 10:
#         return kwargs.keys()
# print(alik(b=2,c=3,d=4,v=5,e=6,g=15))

# client = {
#     'username':'admin',
#     'password':'1234'
# }

# def auth(user):
#     def check_user(func):
#         if user.get("username") == 'admin' and user.get("password"):
#             return func
#         else:
#             print("Acceses danied!")
#     return check_user

# @auth(client)
# def profile():
#     print("Welcome!")

# @auth(client)
# def shop():
#     print("Sale")

# profile()
# shop()

# task - 1

# import calendar

# data = [
#     {"date": (2018, 10, 11)},
#     {"date": (2017, 1, 1)},
#     {"date": (2016, 12, 9)},
#     {"date": (2015, 4, 19)},
#     {"date": (2020, 6, 23)},
#     {"date": (2021, 7, 3)},
#     {"date": (2023, 10, 13)},
# ]

# for i in data:
#     year, month, day = i["date"]
#     cal = calendar.month(year, month)
#     print(cal)

a = 1
def nom():
    a = 2
    print(a)
print(a)