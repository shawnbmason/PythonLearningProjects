# this is the use of .zip() "combins two list together" dictionary
songs = ["Like a Rolling Stone", "Satisfaction", 
         "Imagine", "What's Going On", "Respect", 
         "Good Vibrations"]

playcounts = [78, 29, 44, 21, 89, 5]

plays = {song:playcount for song, playcount in zip(songs, playcounts)}

# this is the use of replacing/adding strings/intigers to the list
plays["Purple Haze"] = 1

plays["Respect"] = 94

# this creates a new key for the existing list
library = {"The Best Songs":plays, "Sunday Feelings":{}}

print(plays, "\n")
print(library, "\n")

# this action displays/prints the list of a specific key that is called
# inside of print()
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], 
                   "fire": ["Aries", "Leo", "Sagittarius"], 
                   "earth": ["Taurus", "Virgo", "Capricorn"], 
                   "air":["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["earth"], "\n")
print(zodiac_elements["fire"], "\n")

# adding new key:value to the dictionary
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], 
                   "fire": ["Aries", "Leo", "Sagittarius"], 
                   "earth": ["Taurus", "Virgo", "Capricorn"], 
                   "air":["Gemini", "Libra", "Aquarius"]}

zodiac_elements["energy"] = "Not a Zodiac element"

print(zodiac_elements["energy"], "\n")

# when the key word is not on the dictionary
wrong_caffeine_level = {"espresso": 64, "chai": 40, 
                        "decaf": 0, "drip": 120}
key_to_check = "matcha"

try:
  print(wrong_caffeine_level[key_to_check])
except KeyError:
  print("Unknown Caffeine Level", "\n")

# when the key word is on the dictionary
caffeine_level = {"espresso": 64, "chai": 40, 
                  "decaf": 0, "drip": 120, "matcha": 30}
key_to_check = "matcha"

try:
  print(caffeine_level[key_to_check], "\n")
except KeyError:
  print("Unknown Caffeine Level", "\n")
  
# this is the use of .get() dictionary
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, 
            "samTheJavaMaam": 123112, "lyleLoop": 102931, 
            "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)
stack_id = user_ids.get("superStackSmash", 100000)

print(stack_id)
print(tc_id, "\n")

# this is the use of .pop() "Delete a Key" dictionary
available_items = {"health potion": 10, "cake of the cure": 5, 
                   "green elixir": 20, "strength sandwich": 25, 
                   "stamina grains": 15, "power stew": 30}

health_points = 20

health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(health_points)
print(available_items, "\n")

# this is the use of .keys() dictionary. Only prints the keys
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, 
            "samTheJavaMaam": 123112, "lyleLoop": 
              102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, 
                 "control flow": 15, "loops": 22, "lists": 19, 
                 "classes": 18, "dictionaries": 18}

# dict_keys or ".keys()"
users = user_ids.keys()
lessons = num_exercises.keys()

print(users)
print(lessons, "\n")

# this is a way you can just get a list of keys
user_id_keys = list(user_ids)
num_exercises_keys = list(num_exercises)

print(user_id_keys)
print(num_exercises_keys, "\n")

# another way to print just the keys outside of a list with a for loop
for users_keys in user_ids.keys():
  print(users_keys)
print("\n")

for nums_exercises_keys in num_exercises.keys():
  print(nums_exercises_keys)
print("\n")
  
# this is the use of .values() dictionary. Only prints the values
num_exercises = {"functions": 10, "syntax": 13, 
                 "control flow": 15, "loops": 22, "lists": 19, 
                 "classes": 18, "dictionaries": 18}

total_exercises = 0

# will take and add the sum of each values one by one
for num in num_exercises.values():
  total_exercises += num
  print(total_exercises)
print("\n")

# use .items() dictionary to print out both keys and values with a for loop
pct_women_in_occupation = {"CEOs": 28, "Engineering Managers": 9, 
                           "Pharmacists": 58, "Physicians": 40, 
                           "Lawyers": 37, "Aerospace Engineers": 9}

for company, number in pct_women_in_occupation.items():
  print("Women make up " + str(number) + " percent of " + str(company))
print("\n")

# here is a fun little game for the end of dictionaries
tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	
  "The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	
    "The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	
      "The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	
        "The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	
          "The Devil", 16:	"The Tower", 17:	"The Star", 18:	
            "The Moon", 19:	"The Sun", 20:	"Judgement", 21:	
              "The World", 22: "The Fool"}

spread = {}

spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

for key, value in spread.items():
  print("Your " + str(key) + " is the " + str(value) + " card.")
print("\n")

# ----------------------------------------------------------------------------------------

# LAST PROJECT
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", 
           "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
           "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 
          1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key: value for key, value in zip(letters, points)}
letter_to_points[" "] = 0
print(letter_to_points)

def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total

brownie_points = score_word("BROWNIE")
print(brownie_points)

player_to_words = {
  "player1": ["BLUE", "TENNIS", "EXIT"],
  "wordNerd": ["EARTH", "EYES", "MACHINE"],
  "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
  "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}
