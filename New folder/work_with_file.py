from faker import Faker

# f = Faker() # fake ma'lumotlarni hosil qilish obyekti
fake = Faker()
# open() = fayllar bilan ishlash va ularni ochish uchun funksiya

# f = open("./test.txt", mode="r", encoding='utf-8')

# r - read, o'qish
# r+ - read + write , o'qish va yozish
# w - write, yozish
# w+ - read + write, o'qish va yozish
# a - append, write, yozish
# a+ - read + write, o'qish va yozish
# x - faylni hosil qilish rejimi (agar fayl oldindan mavjud bo'lsa xatolik vujudga keladi: FileExistsError;)
# x+ - faylni hosil qilish o'qish va yozish rejimi (agar fayl oldindan mavjud bo'lsa xatolik vujudga keladi: FileExistsError
# b - binary, binar rejim fayl methodlari bytes ma'lumot turini qaytaradi
# print(f) # <_io.TextIOWrapper name='./test.txt' mode='r' encoding='utf-8'>
# print(dir(f))

# print(f.read()) # faylni o'qish
# f.close() # faylni yopish

# f = open("./test.txt", mode='a+', encoding='utf-8')
# for i in range(100):
#     fake_name = fake.name()
#     f.write(f'{fake_name}\n')

# task - 1
# import random
# country = [fake.country() for _ in range(15)]
# nums = [f"{random.randint(1, 99)} {random.randint(100, 999)} {random.randint(1, 9)}{random.randint(0, 9)}0" for _ in range(15)]
# with open('country.txt', 'w') as file:
#     file.write(f'{country} {nums}\n')

# task - 2
# from math import ceil
# from random import randint as r_int


# number = ""
# text = str(r_int(0,20000000000))
# start = 0
# end = 3
# if len(text)%3 != 0:
#     end = len(text)%3
#     text_sp = text[start:end]
#     number += f"{text_sp} "
#     start = end
#     end += 3
# for i in range(ceil(len(text)/3)):
#     text_sp = text[start:end]
#     number += f"{text_sp} "
#     start += 3
#     end += 3

# print(number)


# handle = open("./ha.txt", 'w')
# data = handle.write("This is a test!")
# handle.close()

# import this

# import math
# print(math.sqrt(4))