def is_negative(n):
    return n < 0

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    #return n % 2 != 0
    # return n % 2 ==1
    return not is_even(n)
        #function within a function

def is_divisible_by(n, divisor):
    return n % divisor == 0

#def not is_even(6):

## Default value for n = 10, if assign another value: use the other ---> value is optional
def print_stars(n = 10):
    #print("*"*n)
    for x in range(n):
        print("*", end="")
    print()

print_stars()



print( is_negative(7))

print(is_divisible_by(15,3))