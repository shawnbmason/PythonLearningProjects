# .upper(), .title(), and .lower() adjust the casing of your string.
# .split() takes a string and creates a list of substrings.
# .join() takes a list of strings and creates a string.
# .strip() cleans off whitespace, or other noise from the beginning and end of a string.
# .replace() replaces all instances of a character/string in a string with another character/string.
# .find() searches a string for a character/string and returns the index value that character/string is found at.
# .format() allows you to interpolate a string with variables.
# Well I’ve been stringing you along for long enough, let’s get some more practice in!

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
