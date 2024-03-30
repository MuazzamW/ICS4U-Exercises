#public data members - accessible outside class (no getters and setters)

#private datamember - are not accessible outside the class

# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age=age

# s1=Student("John",20)


#protected members - can be accessed outside the class but not directly
#single underscore is used to define protected members
#available to the subclasses

class Student:
    def __init__(self,name,age):
        self._name = name
        self._age=age

s1=Student("John",20)

print(s1._name)

class Teacher(Student):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject