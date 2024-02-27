class Person2:
    def __init__(self,name,sur_name,year_of_birth):
        self._name = name # private
        self.__sur_name = sur_name #protected
        self.year_of_birth = year_of_birth
s = Person2('san','ravindranath',1992)
print(s._name)
print(s.year_of_birth)
print(s._Person2__sur_name)


