# print("\tlorem \npisum")
# r-string
# print(r"lorem\nipsum") # lorem\nipsum

# apple = 10500
# print(f'4 kg olma narxi = {4*apple}') 4 kg olma narxi = 42000


# TASKS

# task - 1
# a = int(input("Soat nechi bo'ldi"))
# if a > 4-1 and a<10+1:
#     print("Hayrli tong !")
# elif a > 10 and a<17+1:
#     print("Hayrli kun")
# elif a > 17 and a<23+1:
#     print("Hayrli kech")
# elif a>23:
#     print("Sizdan soatni soradim axr")
# task - 2
# while True:
#     name = input("Ismingizni kiriting: ")
#     age = int(input(("Yoshingizni kiriting: ")))
#     lengname = int(len(name))
#     result = lengname+age
#     print(result)
#     break

# task - 3
# a = int(input("son kiriting: "))
# b = int(input("2nchi sonni kiriting: "))
# for i in range(a,b+1):
#     print(i)

# task - 4
# a = ["assalomu", "Alaykum12", 'VaAlaykUm55', "AssaLom23"]

# uppercace = 0
# lowercase = 0

# for i in a:
#     for j in i:
#         if j.isupper():
#             uppercace += 1
#         elif j.islower():
#             lowercase += 1

# print(f"Gaplarda {uppercase} ta katta harf va {lowercase} ta kichik harf bor.")


# import locale
# import calendar

# locale.setlocale(locale.LC_ALL, "UZ_uz") # lokal tilini uz tilda qiladi

# cal = calendar.HTMLCalendar() # html calendar obyekti
# cal = calendar.TextCalendar() # oddiy matnli kalendar
# print(cal.formatyear(2023))

# string = "John olmani yeb qoydi , yeb qoydi"
# print("".join(list(filter(lambda x: x != "o", [i for i in string]))))
# a = string.split("o")
# v = "".join(a)
# print(v) # Jhn lmani yeb qydi , yeb qydi

# replace - almashtiradi

# print("assalomu alaykum".replace("a",""))

# print("a1".isalpha()) 

# print("12".isdigit()) # True
# print("1.2".isdigit()) # False

# a = input("Raqamingizni kiriting: ")

# if a.startswith("+"):
#     a = a.replace("+","")
#     if a.startswith("998"):
#         if a.isdigit() and len(a) == 12:
#             print(f"Juda soz Sizning Raqamingiz: {a}")


# isdecimal - 10-xonalik son busa
# print("ONO".isupper()) # True
# print("ono".islower()) # True
# print('Ono'.istitle()) # True 
# print('ONO'.istitle()) # False

# print("   ".isspace()) # true
# print("sasad       ".isspace()) #False

# price = ['fireboox', 'corrupted', 'chrome','corrupted', 'CHROME', 'corrupted']

# for i in range(1, len(price), 2):
#     price[i] = price[i - 1]
# print(price)

# price[1::2] = price[::2]
# print(price)

# user_t = input('matn kiriting: ')
# letters_amazon = '''
# Lorem ipsum dolor sit amet consectetur, adipisicing elit. Officia totam eveniet 
# mollitia modi repudiandae quidem facere labore nisi, et officiis tenetur aperiam quas 
# unde est neque alias molestiae, culpa vero lorem?
# '''

# for i in letters_amazon:
#     for j in user_t:
#         if i.lower() == j.lower():
#             print(i)

# user_t = input('Matn kiriting: ')
# letters_amazon = '''
# Lorem ipsum dolor sit amet consectetur, adipisicing elit. Officia totam eveniet 
# mollitia modi repudiandae quidem facere labore nisi, et officiis tenetur aperiam quas 
# unde est neque alias molestiae, culpa vero loremev?
# '''

# user_t = user_t.lower()
# arr = []

# for i in letters_amazon.lower().split():
#     if user_t in i:
#         arr.append(i)
# result = ', '.join(arr)
# print(result)

# import random

# for i in range(1,20):
#     a = random.randint(1, 25000)
#     print(a, end="  ")