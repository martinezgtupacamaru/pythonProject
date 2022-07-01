first="Guillermo"
last="Martinez"
age="27"

#greetin1g="hello, "+first+" "+last+" you are "+str(age)+" years old."

greeting2="Hello, {} {} you are {} years old".format(first, last, age)

greeting3 = f"Hello, {first} {last} you are {age} years old"
#f is a shortcut to say format, replaces the parantheses with the right values


greeting4="Hello, {1} {0} you are {2} years old".format(first, last, age)

print(greeting4)

print("{:04d}".format(42))

## missing one line, check One Note

print("{:s}".format("42"))
print("{:%}".format(0.42))
print("{:08.2f}".format(12))
#2f = 2 decimals
#total of 8 characters
print("{:8.2f}".format(12))
#padding = spaces, not zeros
print("You owe ${:.2f}".format(12))