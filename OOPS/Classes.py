#Classes Understanding
class Employee:
    def __init__(self):
        self.id=None
        self.name=None
        self.dept=None
        self.salary=None
def Input(emp: Employee):
    emp.id=int(input("Enter Employee ID :"))
    emp.name=input("Enter Employee Name :")
    emp.dept=input("Enter Employee Department :")
    emp.salary=int(input("Enter Employee Salary :"))
def main():
    Emp=Employee()
    Input(Emp)
    print(Emp.id,Emp.name,Emp.dept,Emp.salary)
    print(Emp)

if(__name__=="__main__"):
    main()