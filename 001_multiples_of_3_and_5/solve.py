# If we list all the natural numbers below 10 that are 
# multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of
# these multiples is 23. Find the sum of all the multiples
# of 3 or 5 below 1000.


val = (3 + 999) * (999 / 3) / 2 + (5 + 995) * (995 / 5) / 2 - (15 + 990) * (990 / 15) / 2
print(val)