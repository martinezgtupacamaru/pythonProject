from decimal import Decimal

#Constant value
FEDERAL_TAX = Decimal("0.05")
PROVINCIAL_TAX=Decimal("0.09775")

meal_price=Decimal("44.99")
meal2_price=Decimal("109.99")

price_including_tax=(meal_price*FEDERAL_TAX)+(meal_price*PROVINCIAL_TAX)+meal_price
price_including_tax2=(meal2_price*FEDERAL_TAX)+(meal2_price*PROVINCIAL_TAX)+meal2_price

print(price_including_tax)
print(price_including_tax2)

##Problem 1 = repeating code
##Problem 2 = need to use a constant value (represented by capital letters)

##Solution: constant variable (not expected to change in the run of the code), print at the top:
    #makes more sense (more clear) & no floats? QQQ

##Decimal type system: must import the package (after thought)

from decimal import Decimal

#if give a string: its precise, not ambiguous anymore
x=Decimal("0.05")


##BLABLABLA