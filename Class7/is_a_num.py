## GOOD MASTERS QUESTION

# check if the input is an integer

def check_if_integer(num):
    # try to convert to an integer, it it works, retturn true, else false.

    try: #try 6.9
        int(num)
        return True
    except:
        return False

user_input = input("enter integer.")

# print(check_if_integer((user_input)))

if not check_if_integer(user_input):
    print("Sorry, not integer")

