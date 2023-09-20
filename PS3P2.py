print("Enter the price per share at the time of purchase:")
initialPrice = float(input())
print("Enter the current stock price:")
currentPrice = float(input())
print("enter how much stock you purchased:")
quantityOfStock = float(input())
valueChange = (currentPrice - initialPrice) * quantityOfStock
print("Your value of the stock increased(or decreased) by " + str(valueChange) + ".")
