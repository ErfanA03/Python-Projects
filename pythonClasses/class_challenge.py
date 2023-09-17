"""
#Parent Class
class Employee:
    def __init__(self,name,position,employeeID):
        self.name = name
        self.position = position
        self.employeeID = employeeID

    def punchIN(self):
        print("\n>>>: {} has logged in.".format(self.name))

    def punchOUT(self):
        print("\n>>>: {} has logged out.".format(self.name))


employee1 = Employee("Superman","Chef",1001)
employee1.punchIN()



#Child Class
class Person(Employee):
    def __init__(self, name, position, employeeID, address, email):
        super().__init__(name,position,employeeID)
        self.address = address
        self.email = email

    def Contact(self):
        print("\nAddress: {}\nEmail: {}".format(self.address, self.email))
        
person1 = Person("Batman","Janitor",1002,"The Batcave","bwayne@gmail.com")
person1.punchOUT() #This will call the parent class method.
person1.Contact() #This will call the child class method.
"""

#Polymorphism Assignment

# Parent Class
class Animal:
    #Define the attributes
    def __init__(self, animal_name, gender, species):
        self.animal_name = animal_name
        self.gender = gender
        self.species = species
        
    #Define the methods
    def Information(self):
        print("\nAnimal Name: {}\nGender: {}\nSpecies: {}".format(self.animal_name.capitalize(), self.gender.capitalize(), self.species.capitalize()))



#Child Class
class Pets(Animal):
    #Define the attributes
    def __init__(self, animal_name, gender, species, pet_name, food):
        """
            super().__init__(): This line calls the constructor (__init__ method) of the
            parent class, passing any required arguments to it. This is often done to ensure
            that any initialization code in the parent class is executed before any additional
            initialization in the child class.
        """
        super().__init__(animal_name, gender, species)
        self.pet_name = pet_name
        self.food = food
        
    #Define the methods
    def Information(self):
        print("\nI have a {} named {} who likes to eat {}.".format(self.animal_name, self.pet_name, self.food))



#Child Class
class Reptiles(Animal):
    #Define the attributes
    def __init__(self, animal_name, gender, species, pet_name, food, numOfArms, numOfLegs, cold_blooded):
        super().__init__(animal_name, gender, species)
        self.pet_name = pet_name
        self.food = food
        self.numOfArms = numOfArms
        self.numOfLegs = numOfLegs
        self.cold_blooded = cold_blooded

    #Define the methods
    def Information(self):
        msg = "\nI have a {} named {}, who has {} arms, {} legs".format(self.animal_name, self.pet_name, self.numOfArms, self.numOfLegs)
        if self.cold_blooded:
            print("{} and is also cold blooded!".format(msg))
        else:
            print("{} and is not cold blooded!".format(msg))

my_animal = Animal("cat", "female", "Copurrrnicus") #Create an instance of the "Animal" class
my_pet = Pets("dog", "male", "canine", "Buddy", "dog food") #Create an instance of the "Pets" class
lizard1 = Reptiles("lizard", "female", "reptile", "Lizzy", "insects", 4, 0, True) #Create an instance of the "Reptiles" class

#Polymorphism Examples:
my_animal.Information() #Calls on the Information method from the "Animals" class
my_pet.Information() #Calls on the Information method from the "Pets" class
lizard1.Information() #Calls on the Information method from the "Reptiles" class
