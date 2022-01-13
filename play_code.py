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

#$end
# -------------------------------------------------------------------