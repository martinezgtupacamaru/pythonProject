val=42
val2=44

#compound statement, no need parenthesis, but sometimes yes
if val == 42 and val2==44:
    print("Got here!")
    print("Thanks")
else:
    print("In else statement")

#outside loop, always prints
print("This is the end of the program")

a=33
b=33

#make sure to cover all the bases
if b > a:
    print("b is greater than a")
#Can avoid it by using lots of if
#elif: NECESSARY to make one big chunk
#if's statements are atomic, so not a chunk, the else at the end will only be related to the last if
elif b==a:
    print("b and a are the same")
else:
    print("all other possibilities")

costumer_type= 


