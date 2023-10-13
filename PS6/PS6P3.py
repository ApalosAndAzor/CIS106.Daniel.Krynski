count = 0

prompt = input(f"Would you like to average your score? (Yes/No)")

while prompt == "Yes":
  count = count + 1
  last = input(f"What is your last name? ")
  exam_one = float(input(f"What was your score for the first exam? "))
  exam_two = float(input(f"What was your score for the second exam? "))
  compute = (exam_one + exam_two) / 2
  print(f"{last} your average exam score is {compute}")
  prompt = input(f"Would you like to calculate another student? (Yes/No)")

print(f"This is how many students entered data: {count}")
