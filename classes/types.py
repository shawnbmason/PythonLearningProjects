print(type(5))
# This will output what it is "int/intiger"

my_dict = {}
print(type(my_dict))
# This will output what it is "dict/dictionary"

my_list = []
print(type(my_list))
# This will output what it is "list"

class Facade:
  pass

facade_1 = Facade()

facade_1_type = type(facade_1)
print(facade_1_type)