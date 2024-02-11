import sqlite3
import time
from faker import Faker
# Data base tutorial : sqlite3

con = sqlite3.connect("./main.db", check_same_thread=False) # bu db ga bog'lanish
cur = con.cursor() # db boshqarish obyekti



# sql = """CREATE TABLE students(
#     name TEXT,
#     age INTEGER,
#     gender TEXT,
#     point INTEGER
# );"""

# fake = Faker()
# for i in range(10):
    # sql2 = f"""INSERT INTO students(name,age,gender,point)
    # VALUES('{fake.name()}',{fake.random_int(6,19)},'male',{fake.random_int(30,100)});"""
    # hammasini olish
    # sql3 = """SELECT * FROM students"""
    # point < 90
    # sql3 = """SELECT * FROM students WHERE point < 90"""
    # try:
    #     data = cur.execute(sql3)
    # except sqlite3.DatabaseError as er:
    #     print(er)
    # else:
        # time.sleep(1)
        # print("Success !")
        # con.commit() # o'zgarishni tasdiqlash
#         for data in data.fetchall():
#             print(data)
# con.close()
# con.close()

# task - 1
# text = """
# Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugiat, nulla? Veritatis, minus ad voluptates aperiam amet explicabo qui atque et commodi perspiciatis assumenda fuga laboriosam! Id illo dolore accusantium quia.
# """

# text_arr  = [t.replace("\n"," ").replace("?","").replace(" ","") for t in text.split(" ")]
# print(text_arr)

# data = []
# for i,v in enumerate(text_arr):
#     temp = {
#         "text":v,
#         "index":i,
#         "count":text_arr.count(v)
#     }
#     data.append(temp)

# data.sort(key=lambda x:x["count"], reverse=True)
# print(data[0].get("text"))
# print(data[0].get("count"))

# class Phone:

#     def __init__(self,brand,model,battery,ram,rom):
#         self.brand = brand
#         self.model = model
#         self.battery = battery
#         self.ram = ram
#         self.rom = rom

#     def call(self):
#         print("Call.")
#     def on(self):
#         print("Welcome")
#     def off(self):
#         pass

# p1 = Phone("Apple","14 pro",3200,8,128)
# p2 = Phone("Apple","13 pro max",3000,8,256)

# print(p1.model) # 14 pro
# print(p2.model) # 13 pro max
# print(p1.call()) # Call.
# print(p2.on()) # Welcome

# class Car:
#     company = "Tesla"

#     def main(self):
#         pass

# print(getattr(Car, "company")) 
# print(setattr(Car, "color",'red'))
# print(delattr(Car,"color"))
# print(hasattr(Car,"company"))
# print(hasattr(Car,"color"))

import datetime
class Person:
    def __init__(self, name, surname, birthday):
        self.name = name
        self.surname = surname
        self.birthday = birthday
    def __str__(self):
        return f"My name is {self.name} and my surname is {self.surname}"
    def info(self):
        return f"My name is {self.name} and My sur name is {self.surname}"
    def age(self):
        return f"My old {(datetime.datetime.today().year - 2000)}"
person1 = Person("Mike", "Tyson", 2000)
print(person1.info())
print(person1.age())

# class Phone:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

# Phone2 = Phone("iphone", "black")
# print(Phone2.brand, Phone2.color)


# class Baby(Person):
#     def __init__(self, name, surname, birthday):
#         super().__init__(name, surname, birthday)

# x = Baby("sam", 'asd', '2001')
# print(x.info())

