#Method overriding happens when a child class provides its own implementation of a method already defined in its parent class.
class person:
    def introduce(self):
        print("I am a person")

class Student(person):
    def introduce(self):
        print("I am a student")
person1 = person()
student1 = Student()

person1.introduce()
student1.introduce()