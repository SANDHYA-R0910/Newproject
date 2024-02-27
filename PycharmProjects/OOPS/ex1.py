class Person:

    # def __int__(self,name,surename,emailid,year_of_birth):
    #     self.name = name
    #     self.surename = surename
    #     self.emailid = emailid
    #     self.year_of_birth = year_of_birth
    def __init__(self, name, sure_name, email_id, dob):
        self.name = name
        self.sure_name=sure_name
        self.email_id= email_id
        self.dob=dob


# s = Person("ami", "sandhya", "ami@gmail.com", "2020")
# print(s.name)

s = Person('jan','gun','jan@gmail.com','2020')
print(s.name)
print(s.sure_name)
print(s.email_id)
print(s.dob)

