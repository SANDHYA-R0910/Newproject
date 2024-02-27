class Person:
    def __init__(sudh,name, surname,email, year_of_birth):
        sudh.x = name
        sudh.surname = surname
        sudh.email = email
        sudh.year_of_birth = year_of_birth



    def age(sudh,current_year):
        return current_year - sudh.year_of_birth


s = Person('jan','feb','jan@gmail.com',1994)
print(s.age(2022))
print(s.x + s.surname)
print(s.x)
print(s.surname)
print(s.email)
print(s.year_of_birth)
print(type(s))

s="sudh"
m=s.upper()
print(m)









# class S:
#     def __init__(self, name, l_name, email, dob):
#         self.name = name
#         self.l_name = l_name
#         self.email = email
#         self.dob = dob
#
# s = S("Bala", "krishnan", "bala13@gmail.com", "2-2-2")
# print(s.name)