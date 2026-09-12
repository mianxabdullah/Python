class programmer:
    company="MicroSoft"

    def __init__(self,name,salary,emp_no):  #constructor
        self.name=name
        self.salary=salary
        self.emp_no=emp_no
    
    def __str__(self):   #sort of operator overloading <<
        return f"{self.name} Salary:{self.salary} ID: {self.emp_no}" 

# main logic

p=programmer("harry",120000,1)
print(p.name,p.salary,p.emp_no,p.company)
print(p) #overloading



