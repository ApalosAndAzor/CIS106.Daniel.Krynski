print("How much was your meal?")
totalMeal = float(input())
tipFifteen = totalMeal * 0.15
tipEighteen = totalMeal * 0.18
tipTwenty = totalMeal * 0.2
totalFifteen = totalMeal + tipFifteen
totalEighteen = totalMeal + tipEighteen
totalTwenty = totalMeal + tipTwenty
print("With a 15% tip:")
print("Total: " + str(totalMeal))
print("Tip: " + str(tipFifteen))
print("Total with Tip: " + str(totalFifteen))
print("With a 18% tip:")
print("Total: " + str(totalMeal))
print("Tip: " + str(tipEighteen))
print("Total with Tip: " + str(totalEighteen))
print("With a 20% tip:")
print("Total: " + str(totalMeal))
print("Tip: " + str(tipTwenty))
print("Total with Tip: " + str(totalTwenty))
