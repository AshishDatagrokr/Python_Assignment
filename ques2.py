from abc import ABC, abstractmethod 
class Person(ABC):
    @abstractmethod
    def getGender(self):
        pass

class Female(Person):
    def getGender(self):
        print("Person is Female")


class Male(Person):
    def getGender(self):
        print("Person is Male")


try:
    parent = Person()
except TypeError:
    print(TypeError)
finally :

    print("Female class method")
    female = Female()
    female.getGender()

    print("Male class method")ss
    male = Male()
    male.getGender()




