# try:
#     x = 1/2 # Xatolik bo'lishi mumkin bo'lgan kod
# except Exception as err:
#     print(err) # xatolik topilsa ishlaydigan kod
# else:
#     print('Xatolik yo\'q') # Xatolik bo'lmasa ishlaydigan kod
# finally:
#     print("Barbir ishga tushadigan kod") # barbir ishlaydigan kod

# 1-SyntaxError
# 2-logical
# 3-on working

# BaseException - Barcha xatoliklarni otasi
# Exception - dastur xatori

# email = input('Email ?')

# if "@" not in email:
#     raise ValueError("Email noto'g'ri @ belgi yo'q")
# else:
#     print("To'g'ri")


# data = "1st 2 3-chi 4ta 5 ta 8dona 9 marta 100 200marta"
# nums = []
# for i in data.split(' '):
#     try:
#         num = int(i)
#         nums.append(num)
#     except ValueError:
#         pass
# int_nums = []
# for num in nums:
#     try:
#         int_nums.append(int(num))
#     except ValueError:
#         pass
# print(int_nums)