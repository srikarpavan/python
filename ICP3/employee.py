class Employee():
    empcount = 0 #initialization of the data member
    empsal = []; #list for storing the employees salary
    def __init__(self,name,family,salary,department): #default constructor
        self.empname = name
        self.empfamily = family
        self.empsalary = salary
        self.empdepartment = department
        Employee.empcount +=1  #counts the number of employees
        Employee.empsal.append(salary)  #appends salaray attribute

    def avg_salary(self): #function for the average salary
        print('the average salary is')
        sumsal = 0;
        for sal in Employee.empsal:
            sumsal = sumsal+ int(sal);
        return sumsal/len(Employee.empsal)

class FulltimeEmployee(Employee):
    def __init__(self,name,family,salary,department):
        Employee.__init__(self,name,family,salary,department)


emp1 = FulltimeEmployee('pavan',' chongala','10000','CS');
emp2 = FulltimeEmployee('lakshman','mettu','12000','ECE');
emp3 = FulltimeEmployee('tarun','kasturi','11000','CS');
print("count of the emoloyees",FulltimeEmployee.empcount)  #inherits characteristics from parent class
print(FulltimeEmployee.empsal)
avgsal = FulltimeEmployee.avg_salary(Employee);
print("average salary",avgsal)