while True:
    num1 = input("Enter the first number >")

    try: #Validation is it not a number
        #Validation is the number positive
        if int(num1) > 0:
            break
        else:
            print("Sorry, please enter a positive vibe")

    except:
        print("Sorry, error, try again")

print("Succes -> " + num1)

#     num2 = input("Enter the second number >")
#
#     num_sum = int(num1) + int(num2)
#
#     print(num_sum)
#
# except:
#     print("Sorry, error")