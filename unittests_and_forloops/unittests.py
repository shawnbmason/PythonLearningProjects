import unittest   # The test framework

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(4, 4)

    
#   --------------------------------------------------------------------------------------------------------------------------------------------------      
        
#         def print_some_characters(word):
#             for i in range(len(word)):
#                 if i % 2 == 0:
#                     print(word[i])
 
#         print_some_characters("watermelon")

#         def trip_planner_welcome(name):
#             print("Welcome to tripplanner v1.0" + name)
            
#         trip_planner_welcome(" Shawn Mason ")
 
#         def estimated_time_rounded(estimated_time):
#             rounded_time = round(estimated_time)
#             return rounded_time
        
#         estimate = estimated_time_rounded(2.43)
    
#         def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"): 
#             print("Your trip starts off in" + origin)
#             print("And you are traveling to" + destination)
#             print("You will be traveling by" + mode_of_transport)
#             print("It will take approximately " + str(estimated_time) + " hours to get there")
# #
#         destination_setup(" Mannheim ", " Berlin ", estimate, " Car")
        
        
    
#         def f_to_c(f_temp):
#             c_temp = (f_temp - 32) * 5/9
#             return c_temp
        
#         temp = f_to_c(100)
        
#         print("The temperature is " + str(temp) + " in Celceus and")

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

highlighted_poems_list = highlighted_poems.split(",")

highlighted_poems_stripped = []
for stripped in highlighted_poems_list:
  highlighted_poems_stripped.append(stripped.strip())

highlighted_poems_details = []
for split in highlighted_poems_stripped:
  highlighted_poems_details.append(split.split(":"))

titles = []
for split1 in highlighted_poems_stripped:
  titles.append(split1.split(":")[-3])

poets = []
for split2 in highlighted_poems_stripped:
    poets.append(split2.split(":")[-2])

dates = []
for split3 in highlighted_poems_stripped:
  dates.append(split3.split(":")[-1])

for i in range(0,len(highlighted_poems_details)):
  message = "The {} poem '{}' was written by {}."
  x = message.format(dates[i], titles[i], poets[i])
  print(x)

print("\n", "Dates: ",dates ,"\n")
print("Poets: ",poets, "\n")
print("Titles: ",titles)
          
user = "::::::::::::::::Shawn ::::::::::::::"
user_name_fixed = user.strip(':').strip()

print("\n", user_name_fixed)
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
            # self.busy('Initializing Job data... ')
            # os = 'JOB'
            # genClasses = "Mason"
            # _title_ = "The Man"
            # _version_ = 1.5
            # if os.environ.has_key('JOB'):
            #     self.mode = 'live'
            #     self.job = genClasses.Job(os.environ['JOB'])
            #     if not 'panel' in self.job.steps.keys():
            #         self.job.addStep('panel')
            #         title = _title_ + ' :: ' + _version_ + ' :: ' + self.job.name
            #         self.SetTitle(title)
                
