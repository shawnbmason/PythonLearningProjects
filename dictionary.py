songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {song:playcount for song, playcount in zip(songs, playcounts)}

plays["Purple Haze"] = 1

plays["Respect"] = 94

library = {"The Best Songs":plays, "Sunday Feelings":{}}

print(plays, "\n")
print(library, "\n")

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
  