class employee:
    def __init__(self,name,salary,bonus):
        self.name=name
        self.salary=salary
        self.bonus=bonus
    def __str__(self):
        return f"employee details:\n name={self.name}\n total salary:{self.salary+self.bonus}"

name=input("enter name:")
salary=float(input("enter salary:"))
bonus=float(input("enter bonus:"))

employee_details=employee(name,salary,bonus)
print(employee_details)
