#
# def square(n=0):
#     return n**2

# square("Hello")
# square(square())

def square(n: int):
    return n**2

#Requires an int: allowed to say this is the type that I want the value to be (form of validation)
#it only gives a warning... it will still run (Q !!)

print(square(5.5))