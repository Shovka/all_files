
# choose = 1 ta tasodifiy 1 ta elementni qaytaradi
# sample = siz korsatgan ketma-ketlikdan siz korsatgan miqdorda tasodifiy elemenlarni massiv korinishida qaytardi
# randit - 0 dan  siz korsatgan songa qdar 1ta tasodifiy son qaytaradi.
# randrange - siz kiritgan sonlar 1ta tasodiy sonni qaytaradi

# a = [1,2,4,5]
# shuffle = berilgan massivni elementlarni tasodifiy qilib aralashtiradi

# task - 1 Parol Generatsiya ! 
import random
letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "0123456789"
symbols = "!@#$%^&*()_"
from_data = letters + numbers + symbols

password = ""

pass_len = int(input("Password length ?"))
# for i in range(pass_len):
#     password += random.choice(from_data)
# print(password)
print(''.join(random.sample(from_data, pass_len)))