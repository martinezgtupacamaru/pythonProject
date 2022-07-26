
import random

type_code= "R"
invoice_total=random.randint(0, 1000)
discount=0.0

print(invoice_total)
#conditional statements
if type_code== "R" and invoice_total< 100:
    print("Discount: 0")
elif type_code== "R" and invoice_total>= 100 and invoice_total <250:
    print("Discount: .1")
elif type_code== "R" and invoice_total>= 250:
    print("Discount: .2")
elif type_code== "W" and invoice_total < 500:
    print("Discount: .4")
elif type_code== "W" and invoice_total>= 500:
    print("Discount: .5")

#MORE SIMPLE
if type_code =="R":
    if invoice_total >= 100 and invoice_total <250:
        discount=.1
    elif invoice_total >= 250:
        discount=.2
    #extra logic here... (Nested for Retail "R")
        #Difference between JEDI and PADAWAN
            #Take into consideration feasability, flexibility
if type_code =="W":
    if invoice_total < 500:
        discount =.4
    else:
        discount=.5

print(discount)