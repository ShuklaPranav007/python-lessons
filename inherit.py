class Employee:
    company = "tcs"
    def show(self):
        print(f"the name of Employee is {self.name} and sakary is {self.salary}")

class Programmer(Employee):
    company = "Tcs marathon"
    def showLang(self):
        print(f"the name of Employee is {self.name} and sakary is {self.salary}")

a = Employee()
b = Programmer()
print(a.company, b.company) 