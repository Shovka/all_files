# def my_decorator(num):
#     def wrapper():
#         print('Salom')
#         num()
#         print('alik')
#     return wrapper


# @my_decorator
# def ha():
#     print('ishladi !')
# print(ha())


# class DecoratorTest(object):
#     def __init__(self):
#         """constructer"""
#         pass

#     def doubler(self,x):
#         return x*2

#     @classmethod
#     def class_tripler(klass, x):
#         return x*3
    
#     @staticmethod
#     def static_quad(x):
#         return x*4


# decor = DecoratorTest()
# print(decor.doubler(5))
# print(decor.class_tripler(3))
# print(DecoratorTest.class_tripler(3))
# print(DecoratorTest.static_quad(2))
# print(decor.static_quad(3))
# print(decor.doubler)
# print(decor.class_tripler)
# print(decor.static_quad)


# class Person(object):

#     def __init__(self, first_name, last_name):
#         "constructer"
#         self.first_name = first_name
#         self.last_name = last_name


#     @property
#     def full_name(self):
#         return f"{self.first_name, self.last_name}"


#     def full_name2(self):
#         return f'{self.first_name, self.last_name}'

# person = Person("Mike", "Driscoll")
# print(person.first_name)
# print(person.last_name)
# print(person.full_name2())







print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)

print(8)
print(9)
print(10)
print(11)
print(12)