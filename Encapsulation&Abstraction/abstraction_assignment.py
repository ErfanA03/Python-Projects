# Import the ABC (Abstract Base Class) module to create abstract methods
from abc import ABC, abstractmethod

# Define an abstract class named 'Shape' that inherits from ABC
class Shape(ABC):
    def __init__(self, name):
        self.name = name

    # Define an abstract method 'area' that must be implemented by child classes
    @abstractmethod
    def area(self):
        pass

    # A regular method to display the name of the shape
    def display_name(self):
        print("This shape is called {}".format(self.name))

# Create a child class 'Circle' that inherits from the 'Shape' abstract class
class Circle(Shape):
    def __init__(self, name, radius):
        # Call the constructor of the parent class
        super().__init__(name)
        self.radius = radius

    # Implement the 'area' abstract method for a circle
    def area(self):
        return 3.14 * self.radius * self.radius

# Create an object of the 'Circle' class
my_circle = Circle("Circle", 5)

# Use the regular method 'display_name' from the parent class
my_circle.display_name()

# Use the abstract method 'area' from the child class
circle_area = my_circle.area()
print("The area of the circle is {}".format(circle_area))
