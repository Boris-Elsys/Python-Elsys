from uuid import uuid4

class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def print_employees(self):
        for i in self.employees:
            print(i.name + ", " + i.email)

    def add_employees(self):
        self.employees.append(Employee(input("name: "), input("email: ")))

class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.id = self.gen_id()

    def gen_id(self):
        id = uuid4()
        return id

    def print_atributes(self):
        print("name: " + self.name)
        print("email: " + self.email)
        print("employee id: " + str(self.id))

georgi = Employee("Georgi", "goergi@mail.mail")
georgi.print_atributes()

company = Company("Krastavi Kiselichki")
company.add_employees()
company.print_employees()
