

#Must give 2 values to change the two default values
def animal(name = "Dog", food = "Bones"):
    print(f"A(n) {name} usually eats {food}")

#Positional matching Q !!
animal("cat", "fish")

##Named parameter: replaces the second one
animal(food="Biscuits")

# #CAN NEVER HAVE AN OPTIONAL BEFORE A REQUIRED
#
# def animal(name = "Dog", food):
#     print(f"A(n) {name} usually eats {food}")
#
# animal(food="Biscuits")

##CAN have required before an optional
def animal(name, food = "Bones"):
    print(f"A(n) {name} usually eats {food}")

animal(name="Biscuits")