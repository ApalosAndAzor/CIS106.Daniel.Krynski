#Function - Compute the average score and average score with handicap

def compute(score_one, score_two, score_three, handicap):
  average_score = (score_one + score_two + score_three) / 3
  average_score_handicap = average_score * handicap
  return average_score, average_score_handicap

#Main

last_name = input(f"What is the bowler's last name? ")
score_one = float(input(f"What was the first game score? "))
score_two = float(input(f"What was the second game score? "))
score_three = float(input(f"What was the third game score? "))
handicap = float(input(f"What was the handicap? "))
average_score, average_score_handicap = compute(score_one, score_two, score_three, handicap)
print(f"The last name of the bowler is {last_name}")
print(f"The average score is {average_score:.2f}")
print(f"The average score with handicap is {average_score_handicap:.2f}")
