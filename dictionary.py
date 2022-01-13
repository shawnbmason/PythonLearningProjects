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
wrong_caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
key_to_check = "matcha"

try:
  print(wrong_caffeine_level[key_to_check])
except KeyError:
  print("Unknown Caffeine Level", "\n")

# when the key word is on the dictionary
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120, "matcha": 30}
key_to_check = "matcha"

try:
  print(caffeine_level[key_to_check], "\n")
except KeyError:
  print("Unknown Caffeine Level", "\n")
  
# this is the use of .get() dictionary
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

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

