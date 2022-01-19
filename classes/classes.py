# A class is a template for a data type. It describes the kinds of 
# information that class will hold and how a programmer will 
# interact with that data.

# Class Variables
class Musician:
    title = "Rockstar"
    
drummer = Musician()
print(drummer.title, "\n")

# Class Methods
class Dog:
    dog_time_dilation = 7
    
    def time_explanation(self):
        print("Dogs experience {} years for every 1 human years."
              .format(self.dog_time_dilation), "\n")
        
pipi_pitbull = Dog()
pipi_pitbull.time_explanation()

# Methods with Arguments
class DictanceConverter:
    kms_in_a_miles = 1.609
    def how_many_kms(self, miles):
        return miles * self.kms_in_a_miles

converter = DictanceConverter()
kms_in_a_miles = converter.how_many_kms(5)
print(kms_in_a_miles, "\n")

# More Methods with Arguments
class Circle:
  pi = 3.14
  def area(self, radius):
    return Circle.pi * radius ** 2

circle = Circle()
pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)

print(pizza_area, "\n")
print(teaching_table_area, "\n")
print(round_room_area, "\n")

# Constructors
class Shouter:
    def __init__(self, phrase):
        if type(phrase) == str:
            print(phrase.upper(), "\n")
            
shout1 = Shouter("shout")
shout2 = Shouter("shout")
shout3 = Shouter("let it all out")

# A shorter constructor
class Shouter:
    def __init__(self):
        print("HELLO?!", "\n")

shout1 = Shouter()
shout1 = Shouter()

# Another way to write a construstor
class Circle:
  def __init__(self, diameter):
      print("New circle with diameter: {diameter}".format(diameter = diameter), "\n")
      
teaching_table = Circle(36)

# Instance Variables
class FakeDict:
    pass

fake_dict1 = FakeDict()
fake_dict2 = FakeDict()
    
fake_dict1.fake_key = "This works!"
fake_dict2.fake_key = "This too!"
    
    # joining them together
working_string = "{} {}".format(fake_dict1.fake_key, fake_dict2.fake_key)
print(working_string, "\n")

# Attribute Function
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
    if hasattr(element, "count"):
        print(str(type(element)) + " has the count attribute!", "\n")
    else:
        print(str(type(element)) + " does not have the count attribute :(", "\n")
        
# ***Self in classes***
class Circle:
    pi = 3.14
    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter), "\n")
        
        self.radius = diameter / 2
        
    def circumference(self):
        return 2 * self.pi * self.radius
    
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference(), "\n")

# Everything in an Object
print(dir(5))

def this_function_is_an_object(num):
  return "Cheese is {} times better than everything else".format(num)

print(dir(this_function_is_an_object), "\n")

# String Representation
class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  
  def __repr__(self):
    return "Circle with radius {radius}".format(radius=self.radius)
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room, "\n")

# Last project of Classes
class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)      

class Grade:
  minimum_passing = 65
  
  def __init__(self, score):
    self.score = score
    
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))

# Need to go back through the final project of classes----------------------------------------------------------------
# ------------------------------------------------------