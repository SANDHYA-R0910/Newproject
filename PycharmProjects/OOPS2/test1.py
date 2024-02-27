import test
print(test)
m= test.Person1('jhon','ravindranath',1992)
print(m.year_of_birth)
print(m._name)
print(m._Person1__sur_name)


class Person:
    _name = "san"
    __surname = 'jan'
    yob = 1992

    def _age(self,current_year):
        return current_year - self.yob
    def __age1(self,current_year):
        return current_year - self.yob

obj = Person()
print(obj._age(2022))
print(obj._Person__age1(2023))

class employee(Person):
    _name = "sandy"
    __surname = "man"
    yob = 1993

obj1 = employee()
print(obj1)
#print(obj1._age(2022))
print(obj1._age(2022))
print(obj1.yob)
print(obj1._name)
print(obj1._Person__surname)
print(obj1._employee__surname)


