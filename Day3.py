# Question 1:


''' Design a simple Python class called Car with the following attributes and methods:

Attributes:
make: The make of the car (e.g., Toyota, Ford, etc.).
model: The model of the car (e.g., Camry, Mustang, etc.).
yea
r: The year the car was manufactured.
mileage: The current mileage of the car.

Methods:
__init__(): Constructor method to initialize the attributes of the car.
drive(miles): Method to simulate driving the car for a given number of miles. Update the
mileage attribute accordingly.
display_info(): Method to display the make, model, year, and current mileage of the car.
Create an instance of the Car class, perform some driving operations using the drive()
method, and then display the car's information using the display_info() method.'''


class Car:
    def __init__(self,make,model,year,mileage=0):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        
        
    def drive(self,miles):
        self.mileage += miles   # Mileage is the total number of miles
        
        
    def display_info(self):
        print("Make: " , self.make)
        print("Model: ",self.model)
        print("Year: ",self.year)
        print("Mileage: ", self.mileage)
        
    
    
car = Car(make="BMW", model="5 Series", year=2024)
print("Car's information :")
car.display_info()

car.drive(2100)
print("\n After Driving 2100 Miles:")
car.display_info()
