#Ask user for size of square
#Draw a square of that size

#3

number=input("type a number >")


number=int(number)

for y in range(number):
    for x in range(number):
        print("x", end="")
    print()


##Triangle

for y in range(number):
    for x in range(y+1):
        print("x", end="")
    print()

#OR

for y in range(1, number+1):
    for x in range (y):
        print("x", end="")
    print()

# Use for loops to automate this
# you will need 2 for loops
#you need to convert what the user enters to an interger

##Multiplication table

for y in range(1, number+1):
    for x in range(1, number+1):
        print(str(y*x) + "\t", end="")

    print()





