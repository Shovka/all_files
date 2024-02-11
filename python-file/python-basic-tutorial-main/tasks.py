# task 1 
# Foydalanuvchidan matn qabul qiling , unda "gaz" , "svet", "yo'q" kabi so'zlar ishtirok etganmi yoki yo'qmi aniqlang va ular sonini har birini alohida hisoblab boring so'zlar register turi yoki boshqa qoshimchalar bilan kelishi mumkin bularni ham inobatga oling

# Gaz yo'q ekan lekin svet bor svetamuzika

# gaz = 1
# svet = 2
# text = "Gaz yo'q ekan lekin svet bor svetamuzika gazini bos"
# gaz = 0
# svet = 0
# no = 0
# for t in text.split(" "):
#     if t.lower() == "gaz" or "gaz" in t.lower():
#         gaz += 1
#     if t.lower() == "svet" or "svet" in t.lower():
#         svet += 1
#     if t.lower() == "yo'q":
#         no += 1
# print(f"\ngaz={gaz}\nsvet={svet}\nno={no}")

text = "Gaz yo'q ekan lekin svet bor svetamuzika Gazini bos"
gaz = 0
svet = 0
yoq = 0
for i in text.split(" "):
    if 'gaz'.lower() in i.lower():
        gaz += 1
    if 'svet'.lower() in i.lower():
        svet += 1
    if "yo'q".lower() in i.lower():
        yoq += 1
print(f'Gaz={gaz}\nsvet={svet}\nyoq={yoq}')
# task 2 
# quyidagi shartlarni tekshirib parol togri yoki notogriligini aniqlaydigan dastur tuzing
# password:
#     - minimum 6 ta belgi 
#     - kamida bitta katta harf 
#     - kamida bitta maxsus belgi (/,\,@,/,_,-)

# v = "Salom#Qalesan#Alik#"
# l = len(v)
# card = "8600 1600 2530 1535"
# c = 0
# result = ""

# for i in card.split(" "):
#     if c == 3:
#         result += i
#         print(c)
#     else:
#         result += "**** "
#         c += 1
# print(result)

# task 3 
# n soni berilgan (30 > n > 0) 0 dan n gacha bo'lgan sonlarni orasida probellar bilan chiqaring agar son toq bo'lsa bitta probel bilan uni keyingi son orasini belgilaysiz agar juft bo'lsa 2 ta probel bilan. misol : 0  1 2  3 4  5

# task 4 
# 1 dan  500 gacha sanab barcha 7 sonlarini alohida massivga yozing;
# Masalan nums = [7,17,27……]

sevens = []
for i in range(1,501):
    if "7" in str(i):
        sevens.append(i)
print(sevens)

# print([x for x in range(1,501) if "7" in str(x)])

# task 5
# import random
# user = {
#     "name":"Mike Dean",
#     "key_number":"*****"
# }
#  Ushbu dict  uchun key_number maydoniga name maydoni qiymati uzunligida 1 dan 50 gacha bo’lgan sonlardan tasodifiy sonlar hosil qiling
# key_nums = ""
# for i in range(len(user["name"])):
#     n = random.randint(1,9)
#     key_nums += str(n)
# user["key_number"] = key_nums

# print(user) # {'name': 'Mike Dean', 'key_number': '986572342'}

# task 6 
# Berilgan massivdan sonlarni bir xillarini olib tashlab faqat sanoqdagi ketma-ket sonlarni qoldiring
# Masalan arr = [1,5,6,1,8,5,9]  Output/Javob arr = [1,5,6,8,9]
# Sizga berilgan Massiv bu >> arr = [2,6,6,4,7,8,2,9,7,1,9]

# task 7 

# Kinoteatrda 15 ta qator  bor har bir qatorda 20 tadan o'rin bor. O'rindiqlar seriya raqamlangan
# misol : A12 A bu yerda qator tartib harfi 12 esa  o’rindiq tartib raqami siz foydalanuvchi kiritgan seriya raqamiga qarab o’rindiq qaysi qatorda joylashganini topishingiz kerak. Bundan tashqari random shaklda o’rindiqlar band qilinadi , Kinoteatr 50% ga to’ldiriladi siz foydalanuvchi kiritgan o’rindiq band yoki bosh ekanini chiqarishingiz kerak.

# task 8 
# 9 qavatli uyda 3-ta podyezd bor har bir qavatda 6 tadan kvartira bor. Foydalanuvchi kvartira raqamini kiritsa siz topishingiz kerak;
# (kvartiralar raqamlari 1-chi qavatdan 1-podyezdan boshlanadi : 1-kv , 1-podyezd 1-etaj)
# Kvartira qaysi qavatda ekanini
# Kvartira qaysi podyezdda ekanini



# task 9 
# Istalgan turdagi elementlari mavjud bolgan massivdan faqat sonlarini topib ularni yigindisini hisoblovchi dastur tuzing (Faqat musbat sonlar hisoblanadi)
# l = [True , 1 , 0.3, "one", ["1","uu"]]
# output: 1.3 



# task 10 
# Qiymatlarida butun sonlar berilgan  2 ta dict mavjud siz dictlarda bir xil qiymatga ega elementlarni boshqa random sonlarga almashtirishingiz kerak 
# input:
# a = {"a":5,"b":3}
# b = {"a":2,"b":1, "c":3}
# # output:
# a = {"a":5,"b":8}
# b = {"a":2,"b":6}

# task 11 
# Odil har kuni muntazam 9 soatdan uxlashni reja qilgan. Siz uning uchun u soat nechida uxlashga yotsa roppa rosa 9 soatdan keyin soat nechi bo’lishini hisoblaydigan dastur yozishingiz kerak. Agar Tohir soat 22:00 da uhlashga yotsa demak uyg’onganida soat 07:00 bo’lishini ko’rsatishingiz kerak.
# Kirish : ‘22:00’
# Chiqish : ‘07:00’
# st = "21:30"
# print(abs(9-(24 - int(st.split(":")[0]))) ,":", int(st.split(":")[1])) 
# task 12
# Abdulloh ni Asaka Bank da har oy kirim X mln puli bor va davlatga shu daromad pullaridan 12% daromad solig’i to’lashi kerak. Abdulloh bu yilning 5- oyda davlatimizga qancha soliq to’lashini hisoblang.// x=int(input())

"""
Youtube tasks
"""

# task-1
# def nasisitik(raqam):
#     xona = len(str(raqam))
#     natija = 0

#     for i in str(raqam):
#         natija = natija + int(i)**xona

#     if natija==raqam:
#         return True
#     else:
#         return False

# print(nasisitik(371))

# task-2
# def func2(word):
#     if len(word)<= 4:
#         return word
#     else:
#         part1 = word[:-4]
#         part2 = word[-4:]
#         result = len(part1)*'#'
#         result += part2
#         return result

# a = input("son? ")
# print(func2(a))

# task - 3
# def task3(sentence):
#     all_words = sentence.split()
#     result = []
#     for i in all_words:
#         if len(i)>=5:
#             result.append(i[::-1])
#         else:
#             result.append(i)
#     x = ' '.join(result)
#     return x

# print(task3("Bu python dasturlash tili"))

# task - 4
# a = input("Kiriting: ")
# a = a.split()
# pullar = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 10, 5, 2, 1]

# n = int(a[0]) #Kamol bergan pul
# m = int(a[1]) # mahsulot narxi

# if n<m:
#     print(0)
# else:
#     qoldiq = n-m
#     result = []
#     indexs = 0
#     while indexs <= 14:
#         if qoldiq >= pullar[indexs]:
#             result.append(pullar[indexs])
#             qoldiq = qoldiq - pullar[indexs]
#         else:
#             indexs+=1


# print(result)
# print(len(result))


# task5
# a = input("Hisobni kiriting: ")
# a = a.split("-")

# # birinchi o'yindagi hisob
# roma = 1.1
# barsa = 4

# # 2nchi oyindagi jarayon
# roma2 = int(a[0])
# barsa2 = int(a[1])*1.1

# total_roma = roma + roma2
# total_barsa = barsa + barsa2
# print(f"roma {total_roma} - barsa {total_barsa}")
# if total_barsa>total_roma:
#     print("Lost - Roma yutqazdi")
# elif total_barsa<total_roma:
#     print("Win! - Roma yutdi")
# else:
#     print("penalty")












# task 1
# a = int(input("Soat nechi bo'ldi"))
# if a < 4 or a<10+1:
#     print("Hayrli tong !")
# elif a < 10 or a<17:
#     print("Hayrli kun")
# elif a < 17 or a<23+1:
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

# task - 4 (aniq tushunarlik bo'lmagan)
# a = int(input("son kiriting: "))
# b = int(input("2nchi sonni kiriting: "))
# for i in range(a,b):
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
#     for x in Numbers:
#         if x % 10 == 0:
#             num += x
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
# print(datetime.date(_now.year,_now.month,_now.day) - datetime.date(2007,9,25))


# task - 15
# def find_num(son):
#     for i in range(son + 1):
#         if i % 2 != 0:
#             print(i)

# user_son = int(input("son kiritng: "))
# print(find_num(user_son))