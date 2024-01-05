#----------------------------------------------EXERCISE_1-------------------------------------------------------------------------------------
class Book:
    def __init__(self, title: str, author: str, publication_year: int):
        self.__title  = title
        self.__author = author
        self.__publication_year = publication_year

    def get_info(self)->str:
        return "Title: {self.__title}, Author: {self.__author}, Publication Year: {self.__publication_year}"
    
# Creating an instance of the Book class

hp = Book("Harry Potter", "JK Rowling", 1999)

# displaying attributes using get_info()

print(f"EXERCISE_1: {hp.get_info()}")

#----------------------------------------------EXERCISE_2-------------------------------------------------------------------------------------

class Vehicle:
    def __init__(self, make: str, model: str, year: int, engine_size: str):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__engine_size = engine_size

    def drive(self)->str:
        if (self.__make == "Mercedes") or (self.__make == "BMW") or (self.__engine_size == "Big") or (self.__year > 2010):
            return f"The vehicle sounds like Vroooom phaa!"
        else: 
            return f"The vehicle sounds like vroom!"
    
class Car (Vehicle):
    def __init__(self, make: str, model: str, year: int, engine_size: str, convertible: bool):
        super().__init__(make, model, year, engine_size)
        self.__convertible = convertible 

    def drive(self)->str:
        if self.__convertible == True:
            return f"{super().drive()} with the wind in my hair"
        else: 
           return f"{super().drive()} with some shade"


class Motorcycle (Vehicle):
    def __init__(self, make: str, model: str, year:int,engine_size: str, helmet: str):
        super().__init__(make, model, year, engine_size)
        self.__helmet = helmet

    def drive(self)->str:
        if self.__helmet == "hard":
            return f"{super().drive()} and my head is protected"
        else:
            return f"{super.drive()} and put on a helmet for your safety!"

# Creating an instance for vehicle class
plane = Vehicle("Boeing", "747", 2005, "Big")



# Creating an instance for the Car
        
mercy = Car("Mercedes", "E-class", 2011,"Small", False)

# Creating an instance for the Motorcycle

ducatti = Motorcycle("Ducatti", "500cc", 2012, "Medium", "hard")


print(f"EXERCISE_2, NORMAL VEHICLE: {plane.drive()}")

print(f"EXERCISE_2,Car with vehicle inheritance: {mercy.drive()}")

print(f"EXERCISE_2, Motorcycle with vehicle inheritance: {ducatti.drive()}")
        

#----------------------------------------------EXERCISE_3-------------------------------------------------------------------------------------

class Enginez:
    def __init__(self, size: str, on_off: bool):
        self.__size = size
        self.__on_off = on_off

    def turn_engine_on_off(self):
        if self.__on_off == True:
            self.__on_off = False
            return self.__on_off
        else:
            self.__on_off = True
            return self.__on_off


class Wheels:
    def __init__(self, age: str):
        self.__age = age


class Drivetrain: 
    def __init__(self, number_of_gear: str):
        self.__number_of_gear = number_of_gear

    def shift_gear_up(self):
        self.__number_of_gear += 1
        return f" Gear has been shifted to {self.__number_of_gear}"
    
    def shift_gear_down(self):
        self.__number_of_gear -= 1
        return f" Gear has been shifted to {self.__number_of_gear}"


class Carz:
    def __init__(self, make: str, model: str, year: int,size: str, on_off: bool, number_of_gear: int) :
        self.__make = make
        self.__model = model
        self.__year = year
        self.obj_drivetrain = Drivetrain(number_of_gear)
        self.obj_engine = Enginez(size, on_off)
    
    def movement(self):
        if self.obj_engine.turn_engine_on_off() == True:
            return "The car is a {self.__make} model {self.__model} manufactured in {self.__year} and its {self.obj_drivetrain}"
        else:
            return "The car is off so is not moving."

# Creating an instance of a car
        
bmw = Carz("BMW", "M6", 2018, "medium", False, 3)

print(f"EXERCISE_3: The BMW instance created is: {bmw.movement()}")

#----------------------------------------------EXERCISE_4-------------------------------------------------------------------------------------

# class Team:
#     def __init__(self,studentz:int, employeez:int):
#         self.__studentz = studentz
#         self.__employeez = employeez
    
#     def team_total(self):
#         team_total = self.__studentz  + self.__employeez
#         return f"There are {self.__studentz} students, {self.__employeez} employees and a total of {team_total} team members"


# class Employee:
#     def __init__(self,number_of_employees):
#         self.__number_of_employees = number_of_employees
    
#     def add_employee(self,number_to_add):
#         return self.__number_of_employees + number_to_add

#     def remove_employee(self,number_to_remove):
#         return self.__number_of_employees - number_to_remove


# class Student:
#     def __init__(self,number_of_students):
#         self.__number_of_students = number_of_students

#     def add_student(self,  number_to_add):
#         self.__number_of_students + number_to_add

#     def remove_student(self, number_to_remove):
#         self.__number_of_students - number_to_remove

# employeez = Employee(10).add_employee(30)

# studentz = Student(15)

# team = Team(studentz, employeez).team_total()

# print(team)


#----------------------------------------------EXERCISE_5-------------------------------------------------------------------------------------
class Calculator:
    def __init__(self, *args):
        self.args = args

    def add(self):
        return sum(self.args)
    

three = Calculator(1,2,3)    

print(f"EXERCISE 5: {three.add()}")

#------------------------------------------------------------------------------------------------------------------------------------------------------
