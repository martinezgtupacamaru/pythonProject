num=int(input("Enter an integer greater than 0. >"))

if num<=0:
    print("Sorry the number must be greater than 0.")
if num % 10 == 0:
    print("Multiple of 10")
else:
    print("Not a multiple of 10 ")