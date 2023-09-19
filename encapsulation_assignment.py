class MyClass1:
    def __init__(self):
        self.__private_var = 42  # Private attribute

    def __private_method(self):
        print("This is a private method")

obj = MyClass1()
print(obj.__private_var)  # Raises an error, not accessible outside the class
obj.__private_method()    # Raises an error, not accessible outside the class


class MyClass2:
    def __init__(self):
        self._protected_var = 42  # Protected attribute

    def _protected_method(self):
        print("This is a protected method")

class MyDerivedClass(MyClass):
    def access_protected(self):
        print(self._protected_var)  # Accessing protected attribute from a subclass
        self._protected_method()     # Accessing protected method from a subclass

obj = MyDerivedClass()
obj.access_protected()
