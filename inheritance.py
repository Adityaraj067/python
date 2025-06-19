# class Person:
#     def __init__(self,fname,lname):
#         self.firstname = fname
#         self.lastname = lname
#     def printname(self):
#         print(self.firstname, self.lastname)


# x = Person("aditya","pandey")
# x.printname()
'''
class Animal:
    def __init__(self,name):
        self.name = name
        print({self.name},"the name of animal")
    def speak(self):
        print("a generic sound ehich animal makes")

class Dog(Animal):
    def __init__(self,name,color,breed):
        super().__init__(name)
        self.color = color
        self.breed = breed
    def make_sound(self):
        print("dog barks!! ")
    def print(self):
        print(f"{self.breed}")
obj = Dog("rockey","green","korean")
obj.print()
obj.speak()
obj.make_sound()
   '''     
'''
class Applience:
    def __init__(self,brand,power):
        self.brand  = brand
        self.power = power

class Fan(Applience):
    def __init__(self,brand,power):
        super().__init__(brand,power)
    def fan_obj(self):
        print("fan")
        print(f"fan name {self.brand}")
        print(f"power consumption {self.power}")
        


class Heater(Applience):
    def __init__(self,brand,power):
        super().__init__(brand,power)
    def heater_obj(self):
        print("heater")
        print(f"heater name {self.brand}")
        print(f"power consumption {self.power}")
obj1 = Fan("mst_fan","2000")
obj1.fan_obj()
obj2 = Heater("desi_heater","bina power ke chlta hai")
obj2.heater_obj()
'''
'''
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self,name,age,rollno):
        super().__init__(name,age)
        self.rollno = rollno
    def std1(self):
        print("details of student")
        print(f"name of student is: {self.name}")
        print(f"age of student is: {self.age}")
        print(f"rollno of student is: {self.rollno}")

obj1 = Student("aditya",21,12)
obj1.std1() 
        '''

#   multiple inheritance

class A:
    def method_A(self):
        print("Method A")

class B:
    def method_A(self):
        print("Method B")

class C(A,B):
    def method_A(self):
        print("Method C")

test_obj = C()
print(test_obj.method_A)
