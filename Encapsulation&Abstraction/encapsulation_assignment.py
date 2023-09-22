class MyClass1:
    def __init__(self):
        self.__private_var = 42  # Private attribute

    def __private_method(self):
        print("This is a private method")

    def get_private_var(self):
        return self.__private_var  # Public method to access private attribute


class MyClass2:
    def __init__(self):
        self._protected_var = 42  # Protected attribute

    def _protected_method(self):
        print("This is a protected method")

    def get_protected_var(self):
        return self._protected_var  # Public method to access protected attribute


class MyDerivedClass(MyClass1):
    def access_protected(self):
        # Accessing protected attribute and methods from MyClass2
        base_class = MyClass2()
        print("Protected Var from Base Class: {}".format(base_class.get_protected_var()))
        base_class._protected_method()  # Accessing protected method

        # Accessing private attribute and method from MyClass1
        print("Private Var from Superclass: {}".format(self.get_private_var()))
        self._MyClass1__private_method()  # Accessing private method


obj = MyDerivedClass()
obj.access_protected()
