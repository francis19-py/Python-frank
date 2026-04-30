'''
we'll cover
  __str__(),
  instance vs class varuiables
  @staticmethod
  cleaner object printing
'''

import statistics
class Student:

    school_name = "Tech Academy"#now this belongs to the class itself
    def __init__(self, name):
        self.name = name 
        self.grades = {
        }

    def  add_grades(self, subject, grade):
        self.grades[subject] = grade

    
    def get_average(self):
        if not self.grades:
            return 0 
        return statistics.mean(self.grades.values())

    def __str__(self):
        return f"{self.name} -> {self.grades} | Average: {self.get_average()}"

    

    @staticmethod
    def is_passing(grade):
        return grade >=50

#class variable vs instance variable
#self.name and self.grades belong to each student seperately and that's instance variable



s1 = Student("Frank")
s1.add_grades("math", 80)
s1.add_grades("java", 67)

print(s1)


print(Student.school_name)#throgh the class varialble we can print the school name
print(s1.school_name)

#STATIC METHOD DON'T USE SELF
