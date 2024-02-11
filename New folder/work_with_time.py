import datetime  # sana va vaqt modul
import time # vaqt moduli
import calendar # kalendar moduli

# _now = datetime.datetime.now()
# print(_now) # 2023-09-26 16:39:55.467188
# print(_now.year)
# print(_now.month)
# print(_now.day)
# print(_now.hour)
# print(_now.minute)
# print(_now.second)
# print(_now.microsecond)



# _now = datetime.datetime.now()
# birthday = datetime.date(int(input("Year ")), int(input("Month ")), int(input("Day ")))
# days = datetime.date(_now.year, _now.month, _now.day) - birthday
# days = days.days

# year = days // 365
# ots_month = days % 365
# month = (year * 12) + (ots_month // 12)
# print(month)
# print(f'You Live: Year={year}, month={month} and days={days}')


# import datetime
# import random
# import json

# data = []
# for i in range(1, 20+1):
#     year = random.randint(2000, 2023)
#     month = random.randint(1, 12)
#     day = random.randint(1, 31)
#     hour = random.randint(0, 23)
#     min = random.randint(0, 59)
#     sek = random.randint(0, 59)

#     date_time = datetime.datetime(year, month, day, hour, min, sek)
#     data.append(date_time.strftime("%Y-%m-%d %H:%M:%S"))

# with open("datee.json", "w") as json_file:
#     json.dump(data, json_file)


# a = {
#     'hello':565,
#     'son12':1,
#     'alik':777,
#     'raqam11':23,
# }

# for k in a.keys():
#     if not k.isalpha():
#         print(a[k])

# a = {
#     'hello':2412313,
#     'son12':132143,
#     'alik':121344,
#     'raqam11':23,
#     'aa':102
# }

# for k,v in a.items():
#     if '13' in v:
#         print(k)



# a = {
#     'hello': 2412313,
#     'son12': 132143,
#     'alik': 121344,
#     'cvcc': 22,
#     'aa': 101
# }

# for k,v in a.items():
#     count = 0
#     for i in str(v):
#         count += int(i)

#     if len(k)==count:
#         print(k,v)


# a = {
#     'hello':565,
#     'son12':1,
#     'alik':777,
#     'raqam11':23,
# }

# print(a['hello'])


# n = int(input('n... '))
# a = 1
# b = 1
# c = 0
# for i in range(3,n+1):
#     c = a+b
#     a = b
#     b = c
# print(c)

# a = int(input('son1 '))
# b = int(input('son2 '))

# while a<=b:
#     b = b/a


# if b==1:
#     print('ha')
# else:
#     print('yoq')

# n = int(input('n ? '))
# c = int(input('c ? '))
# a_dict = {}
# for i in range(1, c+1):
#     a_dict[str(i)]=n**i
# print(a_dict)

# a_dict = {
#     'a':2,
#     'a':4
# }

# for k,v in a_dict.items():
#     print(list(filter(lambda x: x==x,k)))



# for i in range(100):
#     print(i)
#     time.sleep(1) # sleep kodini toxtatish , int - sekundlarni qabul qiladi.

# timedelta - vaqt oraligini hisoblash imkoni

# dt1 = datetime.timedelta(weeks=2, days=4, hours=12, minutes=30, seconds=12)
# dt2 = datetime.timedelta(weeks=1, days=1, hours=5, minutes=40, seconds=10)
# print(dt1 - dt2) # 10 days, 6:50:02

# print(datetime.date(2023,10,3)) # 2023-10-03

# c = calendar.TextCalendar()

# c = calendar.HTMLCalendar() # oddiy matn kalendar
# print(c.formatyear(2023)) # yil kalendar
# print(c.formatmonth(2023,10)) # oy kalendar