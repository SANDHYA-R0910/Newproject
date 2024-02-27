# import test1
# obj1 = test1.employee()
# obj = test1.Person()


from utils.util1 import Person2
# import utils.util1

obj = Person2("kumar","monu",2345)
print(obj.year_of_birth)

class Person1:
    def __init__(self,name,sur_name,year_of_birth):
        self._name = name # private
        self.__sur_name = sur_name #protected
        self.year_of_birth = year_of_birth
s = Person1('san','ravindranath',1992)
print(s._name)
print(s.year_of_birth)
print(s._Person1__sur_name)









# class Person:
#     def f1(self,l):
#         self.l = l
#         for i in l:
#             if i == 2:
#                 print(i)
#
# s = Person()
# s.f1([1,2,3,4,5])
