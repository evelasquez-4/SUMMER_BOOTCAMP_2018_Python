class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def getName(self):
        return self.firstname + " " + self.lastname


class Employee(Person):

    def __init__(self, first, last, staffnum):
        Person.__init__(self,first,last)
        self.staffnum = staffnum
    

    def __init__(self,persona,staffnum):
        self.staffnum = staffnum
        self.person = persona

    def getDetalle(self):
        return self.person.firstname +" "+ self.person.lastname+" "+str(self.staffnum)    

    def getInfo(self):
        res = Person.getName(self)
        res += " " + str(self.staffnum)
        return res

p = Person("Mario","Gomez")
e = Employee(p,12)
print(e.getDetalle())