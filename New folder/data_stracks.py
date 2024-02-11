# list - tartibli elementlar ketma-ketligi

# list() , []
# print(list("python")) # ['p', 'y', 't', 'h', 'o', 'n']
# print(list("python", "ddd")) # TypeError: list expected at most 1 argument, got 2

# arr = [1,2,3,4,5]
# print(arr[0]) # 1
# print(arr[len(arr)-1]) # 5 oxirgi element
# print(arr[-1]) # 5 oxirgi element

# print(arr[3]) # 4
# print(arr[-2]) # 4

# arr = [1,2,3,4,5]
# arr[0] = 0
# print(arr) # [0, 2, 3, 4, 5]
# s = "strong"
# s[3] = "i"
# print(s) # TypeError: 'str' object does not support item assignment

# a,b,c = 1,2,3
# print(a+b+c) # 6

# x,z,y = [1,2,3,43,5,34,26,345,23,7] # ValueError: too many values to unpack (expected 3)
# x,z,*y = [1,2,3,43,5,34,26,345,23,7]
# print(x) # 1
# print(z) # 2
# print(y) # [3, 43, 5, 34, 26, 345, 23, 7]


# string = ["Python", "better", "very", "nice", "programming", "language"]
# print(string[1::2])

# matrix = [[1,2,3], [4,5,6], [7,8,9]]

# for i in matrix:
#     for j in i:
#         if j %2==1:
#             print(j**2)
#         elif j%2 ==0:
#             print(j**3)

# lg = [i for i in range(10) if i % 2==0]
# print(lg)

# q = lambda L: q([x for x in L[1:] if x <= L[0] + [L[0]] + q([x for x in L if x > L[0])) if L else []

# task - 1
# result = []
text = """\
Lorem, ipsum dolorr sit amet consectetur adipisicing elit.\
Commodi, et blanditiis! Architecto tempore, sed tenetur quisquam sapiente\
repudiandae labore\
laborum dolorum? Molestias, nihil. Minus ducimus repellendus quia error, vero blanditiis!\
""".split(" ")

# for i in text:
#     if len(i) > 5:
#         result.append(i)


# print(' '.join(result))




# l = []
# for i in range(10):
#     if i %2 == 0:
#         l.append(i)

# print(l) # [0, 2, 4, 6, 8]

# print([i for i in range(10) if i %2==0]) # [0, 2, 4, 6, 8]

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print([x for i in matrix for x in i]) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# l = []
# for x in matrix:
#     for i in x:
#         l.append(i)
# print(l) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# arr = []
# arr.append(0) # bitta element qo'shish uchun
# arr.extend([1,2]) # yangi massiv qoshish uchun
# # arr[5] = 3 # IndexEror
# arr[0] = 1 # massivda mavjud elementni o'zgartirish
# print(arr) # [1, 1, 2]

# arr.insert(0,5)
# arr.insert(10,5) # siz korsatgan indexga siz korsatgan elemetni qoshib beradi

# print(arr) # [5, 1, 1, 2, 5]

# arr = [1,2,3,4]
# arr.pop(0) # siz korsatgan indexdan elementni ochiradi
# arr.pop() # agar index berilmasa oxirgi elemetni ochiradi
# print(arr) # [2, 3]

# arr = [1,2,3,4]
# # del arr[0]
# # print(arr) # [2, 3, 4]
# # del arr[:2]
# # print(arr) # 4
# arr.clear() # massivni tozalaydi
# arr2 = arr.copy() # Nusxasini oladi
# print(arr) # []
# print(arr2) # []

# arr = list("python")
# p = "p" if "p" in arr else "not found"
# print(p)

# print("bor" if 7 in list(range(1,11)) else "yoq")


# arr = [0]
# print(any(arr)) # agar massiv ichida 1dona bolsa ham boolenda true qiymatga ega element bolsa 
# # true qaytaradi aks holda false qaytaradi

# print(all(arr)) # 

# one = []
# two = []
# three = []
# four = []
# fifth = []
# total = list(range(1,50+1))
# for i in total:
#     if i>1-1 and i<10+1:
#         one.append(i)
#     elif i>10-1 and i<20+1:
#         two.append(i)
#     elif i>20-1 and i<30+1:
#         three.append(i)
#     elif i>30-1 and i<40+1:
#         four.append(i)
#     elif i>40-1 and i<50+1:
#         fifth.append(i)
# print(f'1dan 10gacha: {one}\n10dan 20gacha: {two}\n20dan 30gacha: {three}\n30dan 40gacha: {four}\n40dan 50gacha: {fifth}')



# intt = []
# bools = []
# strs = []
# floatt = []
# a = [1,23,True,False,1.2,"s","str",5.68]
# for i in a:
#     if type(i) == int:
#         intt.append(i)
#     elif type(i) == bool:
#         bools.append(i)
#     elif type(i) == str:
#         strs.append(i)
#     elif type(i) == float:
#         floatt.append(i)
# print([intt,bools,strs,floatt])


# import random
# arr = [1,2,3,4,5,6,7]
# print(random.choice(arr))
# arr = [1,2,3,4,5,6,7]
# random.shuffle(arr)
# print(arr)
# arr_2 = random.sample(arr, 3)
# print(arr_2)
# arr = [1,2,3,4,5,6,7,32,432,1]
# arr.sort()
# print(arr)

# sorted() - berilgan ketma-ket qilib beradi
# arr = [1,2,3,4,5,6,7,32,432,1]
# print(sorted(arr))

# tuple - ozgarmas elementlar ketma-ketligi

# set - unikal elementlar to'plami
# s = {}
# s = set()

# s = set("assalom")
# print(s) # {'m', 'a', 'l', 's', 'o'}

# united_set = set("pyt").union({"h","o","n"})
# print(united_set)
# dict - lug'at, elementlariga indeks orqali emas balki kalit so'z orqali 
# murojaat qilinadigan elementlar top'lami

# d_1 = dict(a=10,b=20)
# print(d_1)
# print(d_1.keys()) # dict keys dict_keys(['a', 'b'])
# print(d_1.items()) # dict items tuple objact dict_items([('a', 10), ('b', 20)])
# print(d_1.values()) # dict values dict_values([10, 20])

# print(d_1["a"]) # 10
# print(d_1["b"]) # 20
# print(d_1["a"]+ d_1["b"]) # 30


# print(d_1["some_key"]) #KeyError: 'some_key'
# print(d_1.get("some_key")) # None

# d_2 = {
#     'name':'John',
#     'surname':'Doe'
# }
# print(d_2)

# a = ''.join(["abc:123", "cde:456" , "a:12345","777:xyz"])
# b = ''.join(["abc:456", "cde:123", "a:xyz", "777:12345"])

# a = input('Enter ...')
# b = a.count('-->')
# c = a.count('<--')
# print(b+c)

# a = input("Bilet kiriting: ")
# a = [int(x) for x in a]  # Bilet raqamlarini int tipiga aylantiramiz

# birinchi = a[0:3]
# ikkinchi = a[3:]

# b_result = sum(birinchi)
# i_result = sum(ikkinchi)

# if b_result == i_result:
#     print("Omadli Bilet !")
# else:
#     print("Omadsiz bilet")

# print(sum(1,23,2))

# d = {}
# d.get() - kalit orqali qiymatni olish
# d.pop() - kalit orqali o'chirish
# d.setdefault() - kalit orqali qiymat qoshish yoki olish
# d.items() - dict elementlarini kortej korinishi
# d.keys() - dict qiymatlarini kortej korinishi