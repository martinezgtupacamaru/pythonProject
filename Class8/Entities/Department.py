from decimal import Decimal

class Department():
    name = ""
    code = ""

    def __init__(self, name: str, code:str):
            #protective coding: the more information you provide the better
        self.name = name
            #the name of the object which is going to be taken from the class section, will be equal to the name in this section
        self.code = code