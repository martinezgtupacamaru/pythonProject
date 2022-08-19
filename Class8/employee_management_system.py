from Entities.Worker import *
from Entities.Department import *

#From here it classes become concrete
##Change department name here, changes it in the following sections (i.e. workers)
retail_dept = Department("Medium", "R01")
# retail_dept.name = "Retail"
# retail_dept.code = "R01"
    #has to do with foreign key QQQ*

# w1 = Worker("Guillermo", "Martinez", retail_dept, Decimal("200000.00"))
e1 = Employee("Guillermo", "Martinez", retail_dept, Decimal("20000.00"))
    #constructor
# w1.first_name = "Guillermo"
# w1.family_name = "Martinez"
# w1.salary = Decimal ("200000.00")
# w1.department = retail_dept
    #this worker belongs to this department

# w2 = Worker("Africa", "Martin", retail_dept, Decimal("300000.00"))
e2 = Employee("Africa", "Martin", retail_dept, Decimal("30000.00"))
# w1.first_name = "Africa"
# w1.family_name = "Martinez"
# w1.salary = Decimal ("200000.00")
# w1.department = retail_dept
    #*foreign key: ensures that data is the same for the same reference

c1 = Consultant("Brad", "Johnson", retail_dept, Decimal("60.00"))
c2 = Consultant("Mama", "Brown", retail_dept, Decimal("75.00"))

# Tell me the sum of all salaries and payments for workers for the whole year

worker_roster = [e1, e2, c1, c2]

yearly_amount = Decimal("0.00")

for w in worker_roster:
    yearly_amount += w.get_yearly_pay_amount() #polymorphism: NEED to name this method the SAME for both

print(yearly_amount)

##POLYMORPHIC
    # for each individual in this list, i will take each individual and ask what's its yearly paid amount
    #depending on which type on worker it is, it will calculate it differently Q !!
    #Exact type of behavior is different depending on which type of object it is 


# print(e2.first_name)
# print(e2.department.name)

