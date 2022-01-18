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


# this will seperate the list by the list with whatever the deliniter is
import csv

with open("emails.csv") as email_csv:
  email_reader = csv.DictReader(email_csv, delimiter="@")
  for email_list in email_reader:
    print(email_list, "\n")


# Here’s how we’d create a list of the email addresses of all 
# of the users in the above table:

import csv

list_of_email_addresses = []
with open("users.csv", newline="") as users_csv:
  user_reader = csv.DictReader(users_csv)
  for row in user_reader:
    list_of_email_addresses.append(row["Email"])
    print(list_of_email_addresses, "\n")
  
# This will add a list to the file specified
access_log = [{'time': '08:39:37', 'limit': 844404, 
               'address': '1.227.124.181'}, 
              {'time': '13:13:35', 'limit': 543871, 
               'address': '198.51.139.193'}, 
              {'time': '19:40:45', 'limit': 3021, 
               'address': '172.1.254.208'}, 
              {'time': '18:57:16', 'limit': 67031769, 
               'address': '172.58.247.219'}, 
              {'time': '21:17:13', 'limit': 9083, 
               'address': '124.144.20.113'}, 
              {'time': '23:34:17', 'limit': 65913, 
               'address': '203.236.149.220'}, 
              {'time': '13:58:05', 'limit': 1541474, 
               'address': '192.52.206.76'}, 
              {'time': '10:52:00', 'limit': 11465607, 
               'address': '104.47.149.93'}, 
              {'time': '14:56:12', 'limit': 109, 
               'address': '192.31.185.7'}, 
              {'time': '18:56:35', 'limit': 6207, 
               'address': '2.228.164.197'}, 
              {'time': 'This is my time', 'limit': ' This is my limit ', 'address': ' This is my address'}]
fields = ['time', 'address', 'limit']

import csv

with open("addresses.csv", "w") as logger_csv:
  log_writer = csv.DictWriter(logger_csv, fieldnames=fields)
  log_writer.writeheader()
  for item in access_log:
   log_writer.writerow(item)  


# Reading a JSON file
import json

with open("message.json") as message_json:
  message = json.load(message_json)
  
  print(message['text'])
  
# Writing a JSON file
data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

import json

with open("message_write.json", "w") as data_json:
  json.dump(data_payload, data_json)

# import csv

# compromised_users = []
# with open('passwords.csv') as password_file:
#   password_csv = csv.DictReader(password_file)
#   for password_row in password_csv:
#     compromised_users.append(password_row['Username'])
  
# with open("compromised_users.txt", "w") as compromised_user_file:
#   for compromised_user in compromised_users:
#     compromised_user_file.write(compromised_user)

# import json

# with open("boss_message.json", "w") as boss_message:
#   boss_message_dict = {'recipient': 'The Boss', 'message': 'Mission Success'}
#   json.dump(boss_message_dict, boss_message)