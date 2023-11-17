#Function - Compute the total points and average score

def compute(exam_one, exam_two, exam_three):
  total_points = exam_one + exam_two + exam_three
  average_score = total_points / 3
  return average_score, total_points

#Main

last_name = input(f"What is the student's last name? ")
exam_one = float(input(f"What is the first exam score? "))
exam_two = float(input(f"What is the second exam score? "))
exam_three = float(input(f"What is the third exam score? "))
average_score, total_points = compute(exam_one, exam_two, exam_three)
print(f"The last name of the student is {last_name}")
print(f"The total points is {total_points:.2f}")
print(f"The average score is {average_score:.2f}")
