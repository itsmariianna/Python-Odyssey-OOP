# Design a class Employee with private attributes employee_id, name, and salary. Provide methods to set and get these values. Ensure that salary cannot be negative.

class Employee:

    def __init__(self, employee_id, name, salary):
        self.__employee_id = employee_id
        self.__name = name
        self.__salary = salary if salary >= 0 else 0

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id
    
    def get_employee_id(self):
        return self.__employee_id
    
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_salary(self, salary):
        if salary < 0:
            print("Salary can't be negative")
            self.__salary = 0
        else:
            self.__salary = salary
    
    def get_salary(self):
        return self.__salary

if __name__=="__main__":
    person = Employee(123, "Bob", 600)

    print(f'ID: {person.get_employee_id()}\nName: {person.get_name()}\nSalary: {person.get_salary()}')

    person.set_salary(-2000)

    print(f'Updated price: {person.get_salary()}')