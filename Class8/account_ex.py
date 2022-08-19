class Account:
    balance = 0.00
    active = True
    interest_rate = 0.00

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

# class Checking(Account):
#
#     def withdraw(self, amount):
#         pass

class Savings(Account):

    def withdraw(self, amount):

        if self.balance - amount < 25:
            self.active = False
            print("The balance is less than 25, account is now inactive.")
            super().withdraw(amount)


        if not self.active:
            print("Sorry, cannot withdraw on an inactive account")
        else:
            super().withdraw(amount)


    def deposit(self, amount):

        if self.balance + amount > 25 and not self.active:
            self.active = True

        super().deposit(amount)

savings1 = Savings()
#MAKE A CONSTRUCTOR up
    #Two attributes: starting blance, interest rate)
        #i.e. Savings(Decimal("25.00", Decimal(".01"))


savings1.withdraw(25.00)

print(f"Balance of account is {savings1.balance}")