diners = int(input("How many people on your table? >"))

if diners> 8:
    print("You will have to wait for a table")
else:
    print("Your table is ready")

##best way

diners=int(input("How many people are waiting?"))

print("Your table is ", end="")

if diners >= 8:
    print("not ", end="")

print("ready")

