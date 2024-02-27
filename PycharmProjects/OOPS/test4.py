class Person:

    def __int__(self,name,last_name,email,year_of_birth):
        self.x = name
        self.last_name = last_name
        self.email = email
        self.year_of_birth = year_of_birth

    def __init__(self,name,last_name):
        self.x = name
        self.last_name = last_name

    def age(self, current_age):
        return current_age

s = Person('jan','fan')
print(s.age(2022))

