CHECK_MULTIPLE = 10

while True:
    ##Frist not optimal
    #val=int(input("What is your test value? >")
    val=input("What is your test value? >")
    #Check if user entered "Q" and quit if necessary

    if val.upper()=="Q":
    #if val=="Q" or val =="q":
        break

    val = int(val)

    # if val%10==0:
    #     print("The chosed value is a multiple of 10")
    # else:
    #     print("The chosed value is not a multiple of 10")

    if val % CHECK_MULTIPLE == 0:
        print(f"The chosen value is a multiple of {CHECK_MULTIPLE}.")
        #f == i want you to whenever you look at {} to put in the values
        #print("Yes the value is a multiple of " + str(CHECK_MULTIPLE) + ".")
    else:
        print(f"The chosen value is not a multiple of {CHECK_MULTIPLE}")
print("Quitting program, the chosen value was Q")


