from datetime import date

class Employee:
    
    IncrementalPercent = 1.10
    
    def __init__(self, fullname, age, salary):
        self.fullname = fullname
        self.age = int(age)
        self.salary = int(salary)
        
    def ApplyRaise(self, Raise):
        if Raise is None:
            self.salary = int(self.salary * self.IncrementalPercent)
            return self.salary
        self.salary = int(self.salary * Raise)
        return self.salary
    
    @classmethod
    def ChangeIncrementalPercent(cls, IncrementalChange):
        cls.IncrementalPercent = IncrementalChange
        return IncrementalChange
    
    def IsExperienced(self):
        if self.age >= 25:
            return True
        return False
    
    @staticmethod
    def IsHoliday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return True
        return False

class Coders(Employee):

    IncrementalPercent = 1.30

    def __init__(self, fullname, age, salary, language):
        super().__init__(fullname, age, salary)
        self.lanuage = language

class Manager(Employee):

    IncrementalPercent = 1.05
    
    def __init__(self, fullname, age, salary, empl_list = None):
        super().__init__(fullname, age, salary)
        if empl_list is None:
            self.empl_list = []
        else: self.empl_list = empl_list

    def AddEmployee(self, employee):
        if employee not in self.empl_list:
            self.empl_list.append(employee)

    def RemoveEmployee(self, employee):
        if employee not in self.empl_list:
            self.employee.remove(employee)

    def AllEmployee(self):
        for employee in self.empl_list:
            print("Employee List" ,"-->", employee.fullname)

Emp1 = Employee("Anubhav Gupta", 26, 57000)
Employee.ChangeIncrementalPercent(1.30)
print("Emp1 Experienced --->", Emp1.IsExperienced())
print("Emp1 Original Salary --->", Emp1.salary,"," ,"Emp1 Incremental Salary --->", Emp1.ApplyRaise(None), "Raise --->", Emp1.IncrementalPercent)
print("Checking Holiday --->", Employee.IsHoliday(date(2024, 9, 1)))

# ---- Testing For Employee 2 ---- #

Emp2 = Employee("Ankit Gupta", 20, 10000)
print("Emp2 Original Salary --->", Emp2.salary,"," ,"Emp2 Incremental Salary --->", Emp2.ApplyRaise(1.10), "Raise --->", Emp2.IncrementalPercent)
print("Emp2 Experienced --->", Emp2.IsExperienced())

# ---- Testing SubClasses ---- #

Coder1 = Coders('CamaroBro', 21, 100000, 'Python')
# print(Coder1.fullname)
# print(Coder1.lanuage)

Manager1 = Manager('Morris', '33', '200000', [Emp1])
Manager1.AllEmployee()
Manager1.AddEmployee(Coder1) 
Manager1.AllEmployee()
Manager1.RemoveEmployee(Coder1)