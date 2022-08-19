from decimal import Decimal
# from Department import *

#PARENT CLASSS
class Worker():
    #insert empty values that say which type input should be (e.g. string)
    first_name = ""
    last_name = ""
    department = None
    # salary = Decimal("0.00")
        #always put a string within the Decimal function (static text value in order not to loose any accuracy)

    #Constructor
    # 1) Provide initial values to the new object
    # 2) Do other thing that should happen when the object if created
        #e.g. QQQ?

##dept : department (entrance must be a type department)
    def __init__(self, first: str, family: str, dept): #, salary: Decimal):
            #Can use defensive coding and specify the types
            #can't put an optional b4 a non optional
        self.first_name = first
            #set the first_name of the object to first
        self.family_name = family
        self.department = dept
        # self.salary = salary

#CHILD CLASSES
class Employee(Worker):    #Means: inherit from worker, see the bleu eye at line 5 which means that

    salary = Decimal("0.00")

    def __init__(self, first: str, family: str, dept, salary):
        #When defining Employee, you have to bring up the values including salary in the right order
        self.salary = salary
        super().__init__(first, family, dept)
            #calling the super class, parent class

    def get_yearly_pay_amount(self):  #can do w1.get_yearly_pay_amount() --> will work
        return self.salary

class Consultant(Worker):
    hourly_rate = Decimal("0.00")

    def __init__(self, first: str, family: str, dept, hourly_rate):
        # When defining Employee, you have to bring up the values including salary in the right order
        self.hourly_rate = hourly_rate
        super().__init__(first, family, dept)
        # calling the super class, parent class

    def get_yearly_pay_amount(self):  #BOTH will give you the pay, but goes in two different paths for two different child classes
        return self.hourly_rate * 1950