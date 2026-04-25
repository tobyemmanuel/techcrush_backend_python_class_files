class TechieVersity: #class setup with keywoard "class" followed by class name
     # constructor method called __init__ (a dunder keyword) that works hand in hand with the class during instantiation
    def __init__(this, name, numberOfStudents):
        #adding the instance attribute by assigning the arguments to them
        this.name = name
        this.numberOfStudents = numberOfStudents

    # Our str to provide string data about our class. it is optional
    def __str__(this):
        return f"TechieVersity(name={this.name})"
    
    # custom methods to test the self of the class
    def trackName(this):
        return this.name
    
    def totalFeePaid(this, feeAmount):
        this.feeAmount = feeAmount
        return f"The total fee for the {this.name} {(this.numberOfStudents * feeAmount * this.vat)}"
    
    # attempting to return the value from a static attribute
    def totalFeeNumber(this):
        return this.vat
    
    def carOwners(this):
        return  10
    
    # static attribute or variable within the class. ie it does not change or depend on the class instantiation
    vat = 7.5


# child class inheriting the parent
class Backend(TechieVersity):
    # a child can also have their init or constructor incase you want to pass more data or arguments that is more than the parent
    def __init__(this, name, numberOfStudents, nameOfStudents):
        # using super keyword to instantiate the parent constructor while passing its own expected arguments
        super().__init__(name, numberOfStudents)
        # adding instance attributes for the child
        this.nameOfStudents = nameOfStudents
    
    # Adding custom methods that do not exist in the parent
    def tutor(this):
        return "Tobi"
    
    # atempting polymorphism where this function in the parent takes another form
    def carOwners(this):
        return  100
    
    # using the child's instance attributs
    def studentNames(this):
        return this.nameOfStudents
    
    # calling a static attribute of the parent in the class to show inheritance
    def vatAmount(this, charges):
        return this.vat + charges
    
    
# Instantiating the class
backendTrack = Backend("backend engineering", 200, ["Emmanuel", "Abubakar", "Anthony"])
print(backendTrack.carOwners())
print(backendTrack.vatAmount(200))
# print(backendTrack.tutor())
# print(backendTrack.totalFeePaid(4000))




# # class
# # self
# # __init__
# # return
# # pass
# # def


# # Instance Attribute
# # Class Attribute

# class Car:
#     # Class Attribute
#     wheels = 4

#     def __init__(self, make, model, year = 2022):
#         # Instance Attributes
#         self.make = make
#         self.model = model
#         self.year = year

#     def display_info(self, owner="Unknown"):
#         return f"{owner}'s car is {self.year} {self.make} {self.model} with {Car.wheels} wheels"


# car1 = Car("Toyota", "Camry", 2020)
# print(car1.display_info("Vanessia"))

# car2 = Car("Nissan", "Micra", 2025)
# print(car2.display_info("Azeez"))


class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

result1 = MathUtils.add(5, 3)
print(result1)


# class Animal:
#     def __init__(self, name, leg_count):
#         self.name = name
#         self.leg = leg_count

#     def speak(self):
#         return f"{self.name} makes a sound."

#     def leg_count(self):
#         return f"This animal has {self.leg} legs."

# # animal = Animal("Dog", 4)
# # print(animal.leg_count())


# class Dog(Animal):
#     def __init__(self, name, leg_count, breed):
#         super().__init__(name, leg_count=leg_count)
#         self.breed = breed

#     def speak(self):
#         return f"{self.name} barks."
    
#     def breeding(self):
#         return f"{self.name} {self.breed}."
    
# dog = Dog("Dog", 4, "Bulldog")
# print(dog.breeding())


# __init__

# __str__

# __repr__

# __len__

# __eq__

