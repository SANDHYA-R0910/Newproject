# abstraction: hide a real(data) implementation to a user
class ineuron:
    __students = "datascience"

    def students(self):
        #print("print the class of students",ineuron.__students)
        print(self.__students)

s = ineuron()
s.students()
print(s._ineuron__students)

