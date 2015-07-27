#------------------Attribute Errors ------------------#

################### Example 2 ########################
#Same as example 1, but with an explicit class definition

class Dog:
    def __init__(self, name):
        self.name = name
        self.food = 0
        
    def feed(self):
        self.food += 1
        
fido = Dog("Fido")

fido.bark() #Dogs don't have a bark() method, just a feed() method
