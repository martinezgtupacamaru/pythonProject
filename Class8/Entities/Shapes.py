import math

##Step 1: create classes with attributes and inheritance (based on hierarchy)
class Shape: #PARENT OR GENERALIZATION
    colour = ""

    ##Step 2: add constructors (!!)
    def __init__(self, colour):
        self.colour = colour

class Circle(Shape):  #CHILD OR SPECIALIZATION

    #Data
    radius = 0.00 #not money, so don't have to use Decimals

    def __init__(self, colour, radius):
        super().__init__(colour)  #Get thrown up to the parent, comes back and constructs the colour
        self.radius = radius

    #Methods
    ##STEP 3: POLYMORPHISM
    def get_area(self): #no need parameters
        return math.pi*(self.radius**2)

    def get_perimeter(self):
        return 2*self.radius*math.pi

class Square(Shape):

    side = 0.00

    def __init__(self, colour, side):
        super().__init__(colour)
        self.side = side

    def get_area(self):
        return self.side**2

    def get_perimeter(self):
        return self.side*4

class Rectangle(Square):

    bottom = 0.00 #properties of rectangle: bottom, side and colour

    def __init__(self, colour, side, bottom):
        super().__init__(colour, side)
        self.bottom = bottom

    def get_area(self):
        return self.side*self.bottom

    def get_perimeter(self):
        return (self.side*2)+(self.bottom*2)
