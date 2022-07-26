#while

response = "y"

#any time run a function, must be brackets afterwards
# while response.upper()=="Y":
#     num1=int(input("Enter the first number >"))
#     num2=int(input("Enter the second numbers >"))
#
#     sum_of_numbers = num1+ num2
#
#     print(f"The sum of numbers is {sum_of_numbers}")
#
#     response = input("Again? (y/n)")


response ="y"

while True:
    num1=int(input("Enter the first number >"))
    num2=int(input("Enter the second numbers >"))

    sum_of_numbers = num1+ num2

    print(f"The sum of numbers is {sum_of_numbers}")

    response = input("Again? (y/n)")

    if response.upper()=="N":
        break
