"""
class User:
    #Define the attributes of the class
    name = "No Name Provided"
    email = " "
    password = "1234abcd"
    account_number = 0

    #Define the methods of the class
    def __init__(self, name, email, password, account):
        self.name = name
        self.email = email
        self.password = password
        self.account_number = account

        
    def login(self):
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(self.name))
        else:
            print("You are not authorized for this page.")


class Employee(User):
    base_pay = 11.00
    department = "General"

    
class Customer(User):
    mailing_address = " "
    mailing_list = True

    
#Outside of the class you would create an instance of the User class
new_user = User("John Doe", "jdoe@outlook.com", "p@ssw0rd", 1234)
#Call the login method using the new object
new_user.login()
"""

# Parent class: Vehicle
class Vehicle:
    def __init__(self, brand, year, engine):
        # Define the attributes
        self.brand = brand  # Brand of the vehicle
        self.year = year    # Manufacturing year
        self.engine = engine # Type of engine(Gas/Electric)
        
    # Define the Methods
    def start_engine(self):
        print("{} engine is starting.".format(self.brand))

    def stop_engine(self):
        print("{} engine is stopping.".format(self.brand))


# Child class 1: Car (inherits from Vehicle)
class Car(Vehicle):
    # Define the attributes
    make = " "
    model = " "
    year = 2000

    # Define the Methods
    def honk(self):
        print("The {} is honking!".format(self.make))


class Airplane(Vehicle):
    # Define the attributes
    numOfWings = 0
    numOfPassengers = 0
    maxNumOfPassengers = 4

    # Define the Methods
    def addPassenger(self):
        if numOfPassengers < maxNumOfPassengers:
            numOfPassengers += 1

    def remPassenger(self):
        if numOfPassengers > 0:
            numOfPassengers -= 1


    

