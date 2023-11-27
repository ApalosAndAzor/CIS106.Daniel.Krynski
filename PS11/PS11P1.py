#Function - Display the list name in order

def display_name(last_name):
  for x in last_name:
    print(x)

#Function 2 - Display the list name in reverse order

def display_name_reverse(last_name):
  r = len(last_name)
  for y in range (r-1, -1, -1):
    print(last_name[y])

#Main

last_name = ['Smith', 'Woody', 'Jones', 'Wilson', 'Brown', 'Black', 'White', 'DiCaprio', 'Price', 'Lee']
display_name(last_name)
display_name_reverse(last_name)
