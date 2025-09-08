import itertools
import operator

numbers = [1, 2, 3, 4, 5]

# Calculate the running total using sum, sub, mul,div depending on the function passed
prd = list(itertools.accumulate(numbers,operator.sub))
print(prd)
initial_balance = 1000
transactions = [50, -200, 120, -30, 75]

account_history = list(itertools.accumulate([initial_balance] + transactions))
account_history
