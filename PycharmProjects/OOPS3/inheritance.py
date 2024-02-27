class car:
    def __init__(self,body,engin,tyre):
        self.body = body
        self.engin = engin
        self.tyre = tyre

    def milage(self):
        print('milage of this car')

c = car("solid","v6","radial")
print(c)

class tata(car):
    pass

s = tata("solid1","v66","radial1")
print(s)
print(s.milage())
print(s.body)
