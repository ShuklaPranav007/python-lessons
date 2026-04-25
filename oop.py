class Employee:
    lang= "python"
    sal = 1205469

    def getInfo(self):
        print(f"the lang is {self.lang} the salary is {self.sal}")
    
    @staticmethod
    def greet():
        print("Good morning")
        print("@staticmethod does not need self parameter")

pranav = Employee()
pranav.getInfo()
pranav.greet()