from decimal import Decimal

female_count=0
male_count=0
na_gender=0
not_responded=0

salary_count= 0
salary_total = Decimal("0.00")

# average_salary= Decimal("0.00")
# record_counter=0

with open('input_files/file.txt', encoding='utf-8') as file_object: #variable name
    #contents = file_object.read() #many functions, read take the entire file and puts it inside of contents
    #print(contents.rstrip()) #rstrip(), takes out spaces
    #print(contents)

    # for l in file_object: ##why later does not work if this line is on?
    #     print(l[8:14])
    next(file_object)
# # l for line, s for string QQQ
#     for l in file_object:
#         print(l[8:14])
#         if l[8:15].strip() =="Female":
#             female_count += 1
#         elif l[8:15].strip() == "Male":
#             male_count += 1
#         elif l[8:15].strip()=="Other":
#             na_gender += 1
#         elif l[8:15].strip()== "":
#             not_responded +=1
#
# print(f"Females:{female_count}")
# print(f"Males:{male_count}")
# print(f"Other : {na_gender}")
# print(f"NR: {not_responded}")


    # next(file_object)
    # for l in file_object:
    #     print(l)


    for l in file_object:
        print(" ' " + l[33:40] + " ' ")
        if l[33:40].strip() != "":
            salary_count +=1
            salary_total += Decimal(l[33:40].strip())

#How to round the final print to two Decimals?
salary_average=(salary_total/salary_count)


print(salary_count)
print(salary_total)
print((f"Average salary is : {salary_average}"))
