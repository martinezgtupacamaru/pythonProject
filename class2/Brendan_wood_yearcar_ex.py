## This version is more maintainable

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