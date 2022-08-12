## Nested except

try:
    # print("Do something")
    num1 = input("Enter a numbe 1>")
    num2 = input("Enter a number 2>")

    assert (num2 != "0"), "Sorry your second number cannot be 0."
        #falls into the general category unless create a specific except

    print(int(num1) / int(num2))

except ZeroDivisionError: #Specific exception first
    print("Error: Cannot divide by 0!")

except ValueError: #Specific exception first
    print("Error: One of the numbers you entered is NOT a number.")

except AssertionError as e:
    print(f"Error details: {e}")

except Exception as e: #General exception MUST be at the end, otherwise cancels all others, catches everything else
    print("Error: Unknown error occurred.")
    print(f"The error detail are: {e}")

    