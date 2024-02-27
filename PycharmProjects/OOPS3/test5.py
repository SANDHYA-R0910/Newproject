#encapsulation :  you are not allowing something to modify something directly, but we can modify using method.

class ineuron:
    def __init__(self):
        self.students1 = "datascience"
    def students(self):
        print(self.students1)

m = ineuron()
m.students()
m.students1 = "data analytics"
m.students()

class ineuron1:
    def __init__(self):
        self.__students1 = "datascience"
    def students(self):
        print(self.__students1)
    def student_change(self,new_value): # setter method
        self.__students1 = new_value

n = ineuron1()
n.students()
n.__students1 = "big data"
n.students()
n.student_change("sudh")
n.students()
# m.students1 = "data analytics"
# m.students()