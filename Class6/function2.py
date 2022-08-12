##PUT ALL FUNCTIONS AT THE TOP, name them WELL

# Subroutine
# Function <--

#q f(x0 takes in a first name, a las name, Hello first last
#2 f(x) takes in x and y, returns the sum

#subroutine
def salutation_sub(first, last):
    print(f'Hello, {first} {last}')

#function
def salutation_fn(first, last):
    return f"Hello, {first} {last}"

salutation_sub("Guillermo", "Martinez")

print(salutation_fn("Guillermo", "Martinez"))

# QQQ val or anything else?
def adder(val1, val2):
    return val1 + val2

print(adder(1,2))
