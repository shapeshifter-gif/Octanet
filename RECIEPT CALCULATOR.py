import math

print("Looking to split the cost of a group purchase?\nWelcome to our receipt calculator!")

price_all = eval(input("Step 1: Please input the cost of each meal/product.\n(Note: Eliminate commas)\n"))

tax_p = float(input("Step 2: What is the sales tax in your area?\n(Note: Eliminate % sign)\n"))

tip_p = float(input("Step 3: What percentage would you like to give as a tip?\n(Note: Eliminate % sign)\n"))

split = float(input("Step 4: How many people are you splitting the bill with?\n"))

total_p = (price_all + (price_all * (tax_p / 100.0)) + (price_all * (tip_p / 100.0))) / split

final_p = round(total_p, 2)

print("The total cost per person is: $", final_p)
