# test1 = [12345, "A123", 87]
#
# def is_pass(test_input):
#     if test1[2] > 60:
#         return True
#     else:
#         return False
#
# if is_pass(test1):
#     print("congrats the test was a pass")

##Problems

#Loose
#all sort of errors could occur

##Improvements


# def is_pass(test_input):
#     if test1.get("score", 0) > 60:
#         #goes get score, here does not find it, DANGEROUS
#         return True
#     else:
#         return False
#
# test1 = {"id":12345, "test_id":"A123", "the_score": 87}
#
# if is_pass(test1):
#     print("congrats the test was a pass")

## Problems

#Nothing controling mispelling of categories

### OBJECT ORIENTED CODING

#Model/template: is NEVER run
class Test: #Standard for classes: first letter capital
    id = 0
    test_id = ""
    score = 0

    def __init__(self, id, test_id, score):
        self.id = id
        self.test_id = test_id
        self.score = score


    #define data and function
    def is_pass(self): #Whenever a class function, needs first parameter to be self
                        #self means: is my score greater than 60, I am my own object, did I passed?
        # if self.score > 60:
        #     return True
        # else:
        #     return False
        return self.score > 60


test1 = Test(id=12345, test_id= "A123", score = 87)
test2 = Test(id=23456, test_id= "123", score= 54)
# #test 1 is an object of a type of this class Test, its a test
# ##We are creating object 1 from class: test1, has data bellow <- THIS IS RUN
# test1 = Test()
# test1.id = 12345
# test1.test_id = "A123"
# test1.score = 87
#
# #Second object, each object are distinct, has its own values
# test2 = Test()
# test2.id = 23456
# test2.test_id = "A123"
# test2.score = 54


##Good sorting code
class_test_scores = [test1, test2]

for t in class_test_scores:
    print(f"For student id {t.id} and test {t.test_id} the score was {t.score}")

print("IS test1 value a pass? " + str(test1.is_pass()))
print("IS test1 value a pass? " + str(test2.is_pass()))