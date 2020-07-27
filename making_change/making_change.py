#!/usr/bin/python

import sys

def making_change(amount, denominations):
  # Your code here

  cache = [0] * (amount + 1) 
  if amount < 5:
    for index in range(0,amount):
      cache[index] = 1 

  if amount <= 0:
    return 0

  elif amount < 5 and amount > 0:
    return cache[amount - 1]
  
  else:
    change_50cents = making_change(amount - denominations[-1], denominations)
    change_25cents = making_change(amount - denominations[-2], denominations)
    change_10cents = making_change(amount - denominations[-3], denominations)
    change_5cents = making_change(amount - denominations[-4], denominations)
    change_1cent = making_change(amount - denominations[-5], denominations)

    result = change_50cents + change_25cents + change_10cents + change_5cents + change_1cent

    cache[amount] = result

    return cache[amount]

print(making_change(5, [1, 5, 10, 25, 50]))

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")