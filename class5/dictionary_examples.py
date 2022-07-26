# from decimal import Decimal
#
# # no "" on the left values because they are integer, not strings
# #But why "" on the right values, are they not integers?
# item_prices = {12345678:Decimal("12.99"), 23456789:Decimal("23.99")}
#
# print(len(item_prices))
# print(item_prices[12345678])
#
# #Add an item: key and value
# item_prices[34567890]=Decimal("99.99")
#
# print(item_prices)
#
# # Get the sum of all the prices in that dictionary (need to create another variable)
#
# price_sum=Decimal("0.00")
#
# for i in item_prices:
#     print(i)
#
# print()
#
# for i in item_prices.keys():
#     print(i)
#
# print()
#
# #THIS IS A LIST (Q !!)
# for i in item_prices.values():
#     print(i)
#
# print()
#
# #Returns the whole thing as a Tupple, because it does not make sense to separate them
# for i in item_prices.items():
#     print(i)
#
# #so
#
# sum_of_values=Decimal("0.00")
# for i in item_prices.values():
#     sum_of_values +=i
#
# print(sum_of_values)
#
# #Easier way: because item_prices.values() = LIST
#
# list_of_prices=item_prices.values()
# print(sum(list_of_prices))
#
# # Test existence of a key value (IMPORTANT, works in lists, tupples and dictionaries)
#
# my_tuple = ("A", "B", "C")
# print("A" in my_tuple)

###

# 2D list: list within a list
student_grades= {1:["Brendan", [58.9,77.4,88.4,99]], 2:["Peter",[50.9,45.4,66.4,55]], 3:["June", [65,77,88.4,99.6]]}

print(student_grades)

## Find the lowest grade

# List of 2 items

#print indices: you can further index ... QQQ
print(student_grades[1][1])

lowest_score = min(student_grades[1][1])

print(lowest_score)

#Peter's second score
print(student_grades[2][1][1])

##Why does it not begin at 0 ?? QQQ ITS A DICTIONARY: so no positioning at first?
print(student_grades[0])