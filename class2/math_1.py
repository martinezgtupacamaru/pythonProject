a = 5
b = 6

print(a+a)
print(a + (a * b))
print(a / b)
#print (a / 0)

print(a//b)

print(round(a/b, 2))

print(a ** b)
print(2 ** 2)

print(3 % 2)

# How do we determine if a number is even or off

print(a%2==0)

### Exercise- car purchase

num_purchase = input("What is the purchase year of a car")

num_actual_year = input("What year is it")

print("The number of months since the purchase is")
print((int(num_actual_year)-int(num_purchase))*12)

print("The number of days since the purchase is")
print((int(num_actual_year)-int(num_purchase))*365)

###Brendan Wood version

purchase_year = input("year purchase")
current_year = input("year")

purchase_year=int(purchase_year)
current_year=int(current_year)

years_old=current_year - purchase_year
months_old=years_old*12
days_old=years_old*365

print("Num years old ="+str(years_old))
print("Num years months ="+str(months_old))
print("Num years days ="+str(days_old))

