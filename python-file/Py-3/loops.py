# task-1
# k = int(input("k sonini kiriting: "))
# n = int(input("n sonini kiriting: "))

# for _ in range(n):
#     print(k)
# ================================

# task-2
# a = int(input("a sonini kiriting: "))
# b = int(input("b sonini kiriting: "))
# ================================

# count = 0
# for num in range(a, b+1):
#     print(num)
#     count += 1

# print("Chiqarilgan sonlar soni:", count)
# ================================

# task-3
# a = int(input("a sonini kiriting: "))
# b = int(input("b sonini kiriting: "))

# count = 0
# for num in range(b-1, a, -1):
#     print(num)
#     count += 1

# print("Chiqarilgan sonlar soni:", count)
# ================================

# task-4
# narx = float(input("Bir kilogram konfetning narxini kiriting: "))

# for kg in range(1, 11):
#     total_narx = kg * narx
#     print(f"{kg} kg konfetning narxi: {total_narx}")
# ================================

#task-5
# narx = float(input("Bir kilogram konfetning narxini kiriting: "))

# for kg in range(1, 11):
#     total_narx = kg * 0.1 * narx
#     print(f"{kg * 0.1} kg konfetning narxi: {total_narx}")
# ================================

# task-6 
# narx = float(input("Bir kilogram konfetning narxini kiriting: "))

# for kg in range(12, 21, 2):
#     total_narx = kg / 10 * narx
#     print(f"{kg / 10} kg konfetning narxi: {total_narx}")
# ================================

# task - 7
# a = int(input("a sonini kiriting: "))
# b = int(input("b sonini kiriting: "))

# total_sum = 0
# for num in range(a, b+1):
#     total_sum += num

# print("Butun sonlar yig'indisi:", total_sum)
# ================================

#task - 8
# a = int(input("a sonini kiriting: "))
# b = int(input("b sonini kiriting: "))

# product = 1
# for num in range(a, b+1):
#     product *= num

# print("Butun sonlar ko'paytmasi:", product)
# ================================

# task- 9
# a = int(input("a sonini kiriting: "))
# b = int(input("b sonini kiriting: "))

# sum_of_squares = 0
# for num in range(a, b+1):
#     sum_of_squares += num ** 2

# print("Butun sonlarining kvadratlarining yig'indisi:", sum_of_squares)
# ================================

# task - 10
# n = int(input("n sonini kiriting: "))

# sum = 0
# for i in range(1, n+1):
#     sum += 1/i

# print("Yig'indisi:", sum)
# ================================

# task - 11
# n = int(input("n sonini kiriting: "))

# s = 0
# for i in range(n, 2*n+1):
#     s += i*i

# print("Yig'indi:", s)
# ================================

# task - 12
# n = int(input("n sonini kiriting: "))

# s = 1.0
# for i in range(1, n+1):
#     s *= 1.0 + i / 10.0

# print("Yig'indi:", s)
# =================================
# task - 39
# a = int(input("A..."))
# b = int(input("B..."))

# for i in range(a,b):
#     for j in range(i):
#         print(i)


# n =1
# for j in range(n)
# print(i)



# text = input("Matn kiriting: ")

# gaz = text.count("gaz")
# svet = text.count("svet")
# yoq = text.count("yo'q")

# print("Gaz so'zi", gaz, "martta ishlatilgan")
# print("Svet so'zi", svet, "martta ishlatilgan")
# print("Yo'q so'zi", yoq, "martta ishlatilgan")

# text = input("Matn kiriting: ")
# gaz = 0
# svet = 0
# no =0
# for t in text.lower() == "gaz" or "gaz" in t.lower():
#     gaz += 1
# if t.lower() == "svet" or "svet" in t.lower():
#     svet += 1
# if t.lower() == "yoq" or "yoq" in t.lower():
#     no += 1
# print()
# v = "Salom#Qalesan#Alik#"
# l = len(v)
# res = ""

# for i in v:
#     if l % 2 == 0:
#         if i == "#":
#             i = "("
#     else:
#         if i == "#":
#                 i = ")"
# l -= 1
# res += i

# print(res)


# user_card = int(input("Karta raqam kiriting: "))
# result = ""

# for i in user_card:
# num = input("Enter card num: ") 
# last_num = num[-4:]
# result = "*"*(len(num)-4) + last_num
# print(result)


# n = int(input("Sonni kiriting: "))

# for i in range(n + 1):
#     if i % 2 == 1:
#         print(i, end=" ")
#     else:
#         print(i, end="  ")


# print(" * \t # \t *\n # \t * \t # \n * \t # \t *")

# s= "python"
# arr = [x for x in s if x == 'o']
# print("".join(arr))