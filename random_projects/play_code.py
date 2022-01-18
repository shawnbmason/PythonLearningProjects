# type out python3 in command line then type th following

from datetime import datetime
birthday = datetime(1995, 5, 23, 4, 25, 12)
birthday.year
birthday.month
birthday.day
birthday.hour
birthday.weekday()

datetime.now()
datetime(2022, 1, 12) - datetime(2023, 1, 1)

years = 9731
one_year = 365

how_old = years / one_year

print(how_old)

# find last bit of code in python3 docs datetime
parsed_date = datetime.strptime('Jan 12, 2022', '%b %d, %Y')
parsed_date.month
parsed_date.year
parsed_date.day

date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
date_string

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

students = {key:value for key, value in zip(names, heights)}
print(students)

def shawn(num):
    if num >= 10:
        return True
    else:
        return False
print(shawn(5))
print(shawn(10))
print(shawn(20))
print(shawn(-40), "\n")

def first_name(name):
    if len(name) >= 10:
        return "You have a long name!"
    elif len(name) >= 5:
        return "You have a normal size name."
    elif len(name) >= 3:
        return "You have a short name."
    else:
        return None
print(first_name("Shawn"))
print(first_name("Constantine"))
print(first_name("Ben"))
print(first_name("Ty"))
print(first_name("n"))
print(first_name(""), "\n")


#$end
# -------------------------------------------------------------------