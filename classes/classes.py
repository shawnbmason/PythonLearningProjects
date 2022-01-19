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
print(kms_in_a_miles)

# More Methods with Arguments
class Circle:
  pi = 3.14
  def area(self, radius):
    return Circle.pi * radius ** 2

circle = Circle()
pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)

print(pizza_area)
print(teaching_table_area)
print(round_room_area)
