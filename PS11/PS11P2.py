#Function - Display the list name in order

def display(last_name, exam_score):
  q = len(last_name)
  print(f"In order:")
  for x in range (0, q, 1):
    print(last_name[x], exam_score[x])

#Function 2 - Display the list name in reverse order

def display_reverse(last_name, exam_score):
  r = len(last_name)
  print(f"In reverse order:")
  for y in range (r-1, -1, -1):
    print(last_name[y], exam_score[y])

#Main

last_name = ['Smith', 'Woody', 'Jones', 'Wilson', 'Brown', 'Black', 'White', 'DiCaprio', 'Price', 'Lee']
exam_score = [40, 73, 66, 81, 90, 77, 82, 73, 59, 49]
display(last_name, exam_score)
display_reverse(last_name, exam_score)
