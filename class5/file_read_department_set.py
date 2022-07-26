# departments = set()
# records = []
#
# with open('input_files/file.txt', encoding='utf-8') as file_object:
#     next(file_object)
#
#     for l in file_object:
#
#         records.append(l)
#
#         department = l[56:76].strip()
#
#         #for a set: use add, for a dictionary: use update
#         #Build the set of deepartments
#         departments.add(department)
#
#         #Go through each dept.
#         for d in departments:
#             print(f"TOTAL for {d}")
#
# print(records)


# #Adding, updating and deleting items in a list
# mylist =[]
# mylist.append("A")
# mylist.append("B")
# mylist.append("C")
#
# mylist[2]="HI"
#
# #del(mylist[1])
#
# #subset of a list
# print(mylist[1:3])
#
# #subset of a string
# n ="Guillermo"
# print(n[2:5])

list2=[1,6,8,3,6]

print(sum(list2))

#don't do this for the Homework
print(min(list2))

# There is no average. Use sum divided by len

print(sum(list2)/len(list2))

# #Can't add strings
# list3=["A","B","C","D"]
#
# print(sum(list3))


# # Tuples: cannot modify, only define them
# thistuple=(1,3,7,8,7,5,4,6,8,5)
#
# x=thistuple.index(8)
# print(x)
#
# my_tuple = (1,2,3)
#
# #does not work
# del my_tuple[1]

