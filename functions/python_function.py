def trip_planner_welcome(name):

  print("Welcome to tripplanner v1.0 " + name)

def destination_setup(origin, destination, estimated_time, mode_of_transport):
  print("Your trip starts off in " + origin)
  print(" And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

trip_planner_welcome(" Shawn Mason ")
estimate = estimated_time_rounded(2.43)
destination_setup(" Mannheim ", "Germany ", estimate, "Car")

# ------------------------------------------------------------------------------------------------------------

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")
print(author_names)

author_last_names = []
for name in author_names:
    author_last_names.append(name.split()[-1])
  
print(author_last_names)

#$end

print("hello there")

# Will populate a list of the authors last names