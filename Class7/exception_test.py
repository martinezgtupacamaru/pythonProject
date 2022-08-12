# print(7/0)

# raise Exception("Error, the value must be an integer.")

## Assert to make sure the GPA of the student is above 2.8

try:
    GPA=-4.4
    assert(GPA>2.8), "GPA does not pass the 2.8 threshold."

    assert(GPA >= 0 and GPA <= 4.3), "Error: GPA is not within the accepted range."


    print(GPA)

except:
    print("Sorry, an error has occurred.")

#Can put ANYTHING as long as it evaluates TRUE or FALSE (!!)