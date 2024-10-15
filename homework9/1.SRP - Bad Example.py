class Student:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def save_student(self, database):
        ...
        print(f"{self.name} has been added to the {database} database")
    
    def send_email(self, subject):
        ...
        print(f"Email has been sent to {self.email} with subject: <{subject}>")

person = Student("Bob", 12, "bob@gmail.com")
person.send_email("YOU ARE SELECTED")
person.save_student("Passed exam")
