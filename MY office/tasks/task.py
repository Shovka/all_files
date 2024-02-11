# task-1
# a = "ABCDEFG"
# b = "12345678"
# d = {}

# for i in range(len(a)):
#     d.update({a[i]:b[i]})
# print(d)
# print({k:v for (k,v) in zip(a,b)})

# task-2
# a = 'qwrtpsdfghjklzxcvbnm'
# b = 'eyuioa'
# user = input("so'zni kiriting: ")
# result = ''
# for i in user:
#     for k in a:
#         if i == k:
#             result +=i
#     for j in b:
#         if i == j:
#             result += f"{i} "
# print(result)


#task-3
# questions = [
#     ("9 x 1 = ?", 9),
#     ("9 x 2 = ?", 18),
#     ("9 x 3 = ?", 21),
#     ("9 x 4 = ?", 36),
#     ("9 x 5 = ?", 45),
#     ("9 x 6 = ?", 54),
#     ("9 x 7 = ?", 63),
#     ("9 x 8 = ?", 72),
#     ("9 x 9 = ?", 81),
#     ("9 x 10 = ?", 90),
# ]

# for question, answer in questions:
#     userNum = input(f"{question} ")
#     if userNum.isdigit():
#         if int(userNum) == answer:
#             print("To'g'ri javob!")
#         else:
#             print(f"Xato javob. To'g'ri javob {answer} bo'ladi.")
#     else:
#         print("Faqat sonlarni kiriting!")



# task-4
# userr = input("So'zlar kiriting : ")
# num = 0
# indexs = []

# for i in range(len(userr)):
#     if userr[i].lower() == 'a':
#         num += 1
#         indexs.append(i)

# print(num, indexs)

# week = ['yak', 'dushanba', 'seshanba', 'chorshanba', 'payshanba','juma', 'shanba']

# n = int(input("son"))
# s = n%7
# print(week[s])


# jadval = []
# n = int(input("son ? "))

# if n%2:
#     print("toq")
# else:
#     print("juft")
#     jadval.append()

# a = int(input("son"))
# b = int(input("1"))

# for i in range(a):
#     if i%2:
#         print(f"{i}\ntoq")
#     else:
#         print(f"{i}\njuft")

# def findNum(arr):
#     a = 0
#     for i in arr:
#         if i > 0:
#             a += i
#     return a

# array = [3, -5, 8, 2, -1, 7,10]
# result = findNum(array)
# print(f"Sonlar yig'indisi: {result}")

# while True:
#     a = int(input(f"2* Sonni kirit"))
#     if a == True:
#         print("Javob togri")
#         break
#     else:
#         print("javob notogri")

def user(users):
    for i in users:
        if i == 1:
            print("son")
            return user