# task 1
# a = int(input("Soat nechi bo'ldi"))
# if a > 4-1 and a<10+1:
#     print("Hayrli tong !")
# elif a > 10 and a<17+1:
#     print("Hayrli kun")
# elif a > 17 and a<23+1:
#     print("Hayrli kech")
# elif a>23:
#     print("Sizdan soatni soradim axr")

# task -2
# a = ["assalomu", "Alaykum12", 'VaAlaykUm55', "AssaLom23"]

# uppercace = 0
# lowercase = 0

# for i in a:
#     for j in i:
#         if j.isupper():
#             uppercace += 1
#         elif j.islower():
#             lowercase += 1

# print(f"Gaplarda {uppercace} ta katta harf va {lowercase} ta kichik harf bor.")

# task - 3
# while True:
#     name = input("Ismingizni kiriting: ")
#     age = int(input(("Yoshingizni kiriting: ")))
#     lengname = int(len(name))
#     result = lengname+age
#     print(result)
#     break

# task - 4
# a = int(input("son kiriting: "))
# b = int(input("2nchi sonni kiriting: "))
# for i in range(a,b+1):
#     print(i)

# task - 5 (Ushbu masalaga tushunmadim)

# task-6 (o'tilamagan mavzu xato masala)

# task - 7
# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("ikkinchi sonni kiriting: "))

# for i in range(a,b):    
#     result = []
#     if i %2==1:
#         result.append(i)
#         print(result)

# task - 8
# def all_nums_0(Numbers):
#     num = 0
#     for i in Numbers:
#         if i % 10 == 0:
#             num += i
#     return num


# Numbers = [85, 0, 23, 107, 100, 12, 0, 99, 56, 200,500,101,205,3]
# print(all_nums_0(Numbers))


# task - 9
# a= [7,4,5,3,2,2,3,7,1001,5,51,8,1,2,1]
# c = set(a)
# d = sorted(c)
# print(d)


# task - 10
# import random

# def randomlower(a):
#     result = []
#     for i in a:
#         choice = random.choice([i.upper(), i.lower()])
#         result.append(choice)
#     return ''.join(result)

# _user = input("So'zni kiriting: ")
# print(randomlower(_user))

# task - 11 (o'tilmagan dars va xato masala)


# task - 12
# def unlilar(matn):
#     unlilar = "aeiou"
#     result = 0
#     for i in matn:
#         if i.lower() in unlilar:
#             result += 1
#     return result

# matn = input("Matn kiriting: ")
# print(f"Matningizda {unlilar(matn)}-ta unli harf qatnashdi !")



# task - 13 (o'tilmagan dars va xato masala)

# task - 14
# import datetime
# _now = datetime.datetime.now()
# print(datetime.date(_now.year,_now.month,_now.day) - datetime.date(2007,10,25))


# task - 15
# def find_num(son):
#     for i in range(0, son+1):
#         if i % 2 != 0:
#             print(i)

# user_son = int(input("son kiritng: "))
# print(find_num(user_son))