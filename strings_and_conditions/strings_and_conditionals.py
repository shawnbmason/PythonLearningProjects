def letter_check(word, letter):
  for character1 in word:
    if character1 == letter:
     return True
  return False

print(letter_check("strawberry", "o"))

# outputs False

favorite_fruit = "blueberry"
counter = 0
for character in favorite_fruit:
  if character == "b":
    counter = counter + 1
print(counter)

# outputs 2

def contains(big_string, little_string):
  return little_string in big_string
print(contains('watermelon', 'melon'))

# outputs True

# Project

def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name

print(username_generator("Bob", "Wilson"))

# output BobWils

def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password

print(password_generator("BobWils"))

# output sBobWil