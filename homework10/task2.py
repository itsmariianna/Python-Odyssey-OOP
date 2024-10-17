# Implement insertion sort to sort an array of custom objects (e.g., students) based on a specific attribute (e.g., age or grade).

class Student:
    
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def __repr__(self):
        return f'Name : {self.name} -> Grade : {self.grades}'
    

def insertion_sort_for_grades(list_of_students, key):
    size = len(list_of_students)

    for i in range(1, size):
        j = i

        while getattr(list_of_students[j - 1], key) > getattr(list_of_students[j], key) and j > 0:
            list_of_students[j - 1], list_of_students[j] = list_of_students[j], list_of_students[j - 1]
            j -= 1

    

all_students = [Student("Ann", 95),
                Student("Bob", 86),
                Student("Jane", 76),
                Student("Liam", 90),
                Student("Harry", 68),
                Student("Louis", 74)]

insertion_sort_for_grades(all_students, key = "grades")

for student in all_students:
    print(student)