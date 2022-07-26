departments = {}
with open('input_files/file.txt', encoding='utf-8') as file_object:
    next(file_object)

    for l in file_object:
        department = l[56:76].strip()

        #check if the dept is in the dict.
        #if not, create a new record with "1" as a value
        #if it is, get the value, increase it by 1, and upgrade it.

        print(department)

        if department in departments:
            departments[department]+=1
        else:
            departments[department]=1

    print(departments)