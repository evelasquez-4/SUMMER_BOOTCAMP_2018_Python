class Employe:

    def __init__(self, nombcomp):
        first,last = nombcomp.lower().split(' ')
        self.__first, self._last = first,last
        self.email = first + "." + last + "@email.com"

    @property
    def fullname(self):
        return self.__first + " " + self._last



emp1 = Employe("angelina jolie")
#emp1.fullname = "otra cosa"
print(emp1._Employe__first)
print(emp1._last)
print(emp1.email)
print(emp1.fullname)