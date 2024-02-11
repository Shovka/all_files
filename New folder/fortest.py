# def upperLower(a,b):
#     if a<b:
#         return 'b katta'
#     elif a>b:
#         return 'a katta'
#     else:
#         return 'Sonlar teng'

# q = int(input("1nchi sonni kiriting: "))
# w = int(input("2nchi sonni kiriting: "))

# print(upperLower(q,w))

# user: 7 # 1 / 9
# output: "hayrli tong" # 1 / 9

# user: 13 # 9 / 17
# output: "hayrli kun" # 9 / 17

# user: 18 # 17 / 23
# output: "hayrli kech" # 17 / 23

# user: 35 # 24 / ...
# output: "men szdan soat suradm axr" # 24 / ...


# userNum = int(input("Soat nechi bo'ldi? "))

# if userNum > 1 and userNum < 9+1:
#     print("Hayrli Tong!")
# elif userNum > 10+1 and userNum < 17+1:
#     print("hayrli kun!")
# elif userNum > 18+1 and userNum < 23+1:
#     print("Hayrli kech!")
# else:
#     print("Axr sizdan soat so'radim!")

# import turtle as t
# import colorsys
# t.bgcolor("black")
# h = 1
# t.tracer(200)
# t.pensize(1)
# def drawing(a, n):
#     t.circle(5 + n, 60)
#     t.right(a)
#     t.circle(5 + n, 60)

# t.goto(0, 0)
# for i in range(600):
#     c = colorsys.hsv_to_rgb(h, 1, 0.8)
#     h += 0.005
#     t.pencolor(c)
#     drawing(1/2, 0)
#     drawing(180, i)

# t.done()