answer_list = ["Y", "y", "yep"]

x="y"

#while x=="y" or x=="Yes" or x=="A":

while x in answer_list:
    print("OK continuing")
    x=input("Continue again? >")