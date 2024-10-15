class Student:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

class DatabasedStudent:
    def save_student(self, student: Student, database):
        ...
        print(f"{student.name} has been added to the {database} database")

class EmailService:
    def send_email(self, student: Student, subject):
        ...
        print(f"Email has been sent to {student.email} with subject: <{subject}>")

person = Student("Kate", 16, "kate@gmail.com")

database = DatabasedStudent()
database.save_student(person, "PassedExam")

email_service = EmailService()
email_service.send_email(person, "Congratulations!You have successfully passed exam")
