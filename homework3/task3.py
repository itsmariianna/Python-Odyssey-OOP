# Create a class Student with private attributes name, roll_number, and grades. Implement methods to add grades, calculate the average grade, and display the student’s information. Ensure that the grades are between 0 and 100.

class Student:

    def __init__(self, name, roll_number):
        self.__name = name
        self.__roll_number = roll_number
        self.__grades = []

    def add_grades(self, grade):
        if grade >= 0 and grade <= 100:
            self.__grades.append(grade)
        else:
            self.__grades.append(0)
    
    def avg(self):
        if self.__grades:
            average = sum(self.__grades) / len(self.__grades)
            return average
        else:
            return 0
        
    def info_about_student(self):
        return f'Name: {self.__name}\nRoll number: {self.__roll_number}\nGrades: {self.__grades}\nAverage grades: {self.avg()}'

    
if __name__ == "__main__":

    person = Student("Bob", 34521)
    person.add_grades(67)
    person.add_grades(88)
    person.add_grades(91)
    person.add_grades(-12)

    print(person.info_about_student())
