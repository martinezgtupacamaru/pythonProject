import csv

with open('input_files/100_sales_recs.csv',encoding='utf-8') as file_object:

    next(file_object)

    csv_file_object=csv.reader(file_object) #use csv library and reader from it

    for row in csv_file_object:

        #if row[4]=='H':  #Access to each of the column automaticaly parsed
            #pass

        print(row[3])




# ## What is a list
# my_list= ["A", "B", "C", "D"]
#
# # Acessing list members
#
# print(my_list)
#
# print(len(my_list))
#
# print(my_list[0])
#
# print(my_list[3])
#
# for x in my_list:
#     print(x)

##What is a dictionary
provinces = {"QC":"Quebec","ON":"Ontario","AB":"Alberta"}

#Add another and value
provinces["NB"]= "New Brunswick"

print(len(provinces))

print(provinces["NB"])
#Give me the province for AB -> gives the value
#if use same key, last value overides the one before


## a Set (is a list, without reapeating values)

my_set=set()




