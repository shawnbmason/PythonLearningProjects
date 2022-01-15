print("-----------------This is a project about flies in Python---------------")
# This opens a file object called text_file and creates a new 
# indented block where you can read the contents of the opened file
with open('fileExample.txt') as text_file:
# We then read the contents of the file text_file using text_file.read()
# Also,  save the resulting string into the variable called text data
  text_data = text_file.read()
print(text_data, "\n")

# We can use the .readlines() function to read a text file line 
# by line instead of having the whole thing
with open("fileExample.txt") as lines_doc:
  for some_kind_of_word in lines_doc.readlines():
    print(some_kind_of_word, "\n")
print("\n")

# This will seperate each line in the file into its own veribal
with open('fileExample.txt') as shawn_doc:
    first_line = shawn_doc.readline()
    second_line = shawn_doc.readline()
    print(first_line)
    print(second_line)
print("\n")
 
# This is an action to be able to edit/write in the file 
# Here we pass the argument 'w' to open() in order to indicate to open the file in write-mode
# ***This will also rewright everything in the file***
with open("fileWriteExample.txt", "w") as edit_doc:
    edit_doc.write("What an incedible file! ")
  
# We can open a file with 'a' for append-mode to just add on to the ecxisting file
with open("fileWriteExample.txt", "a") as append_doc:
    append_doc.write("Hello everyone. Coding is great!")
    
with open("fileWriteExample.txt") as read_append_doc:
  read = read_append_doc.read()
  print(read, "\n")

# Here’s how we’d create a list of the email addresses of all 
# of the users in the above table:

# import csv

# list_of_email_addresses = []
# with open("users.csv", newline="") as users_csv:
#   user_reader = csv.DictReader(users_csv)
#   for row in user_reader:
#     list_of_email_addresses.append(row["Email"])
