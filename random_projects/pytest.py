def update_order(new_item, current_order=[]):
  current_order.append(new_item)
  return current_order
 
order1 = update_order({'item': 'burger', 'cost': '3.50'})

order2 = update_order({'item': 'soda', 'cost': '1.50'})
 
print(order2)


import random

name = "Shawn"
question = "Do I stink?"
answer = ""

random_number = random.randint(1, 10)

if random_number == 1:
  answer = "Yes - definitley"
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "doubtful."
elif random_number == 10:
  answer = "Very doubtful."
else:
  answer = "Error"

if name == " " and question == " ":
  print("Please ask a question or a name")
elif len(name) == 0 and len(question) == 0:
  print("Please ask a question or a name")
elif question == " ":
  print("Please ask a question or a name")
elif len(question) == 0:
  print("Please ask a question")
elif name == " " or name == "":
  print("Question:", question)
  print("Magic 8-Ball's answer:", answer)
else:
  print(name, "asks:", question)
  print("Magic 8-Ball's answer:", answer)
  