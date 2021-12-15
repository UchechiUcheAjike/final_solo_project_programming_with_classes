#
# Description:
#   This is the Shape class. It is a super class that 
#   the Square class will be inheriting from.
#
# OOP Principles Used:
#   The Object oriented programming principles used here are Abstraction, Encapsulation, Inheritance


#
# Reasoning:
#   The Abstraction class was used because this code can contain 
#   more shapes if needed, in that case the users only interract
#   with the child classes and not the super class. 

#   The encapsulation was used to create a public variable 
#   which is visible and modifiable by all and a private 
#   visible that is modifiable only by an object/class variable
#   
#   Inheritance was used in the base class Shape and the derived 
#   class Square. Square inherits Shape
#
class Shape(ABC):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

class Square(Shape):  #inheritance
    def __init__(self, side):
        self.__side = side
    def area(self):
        return self.__side * self.__side
    def perimeter(self):  
        return 4 * self.__side


square = Square(2)  # public variable
print(square.area())
print(square.perimeter())

__square = Square(2)  # private variable
print(square.area())
print(square.perimeter())


