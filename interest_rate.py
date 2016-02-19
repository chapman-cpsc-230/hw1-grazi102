
"""
File: <interest_rate.py>

Copyright (c) 2016 <Lauren Graziani>

License: MIT

<calculating interest rate>
"""

A = 1000 # Intial amount in euros
p = 5.0 # interest rate
n = 3 # three years
sum= A * (1 +(float(p)/100)) ** n # float p to ignore integer divison
print "intial amount: %d euros, interest rate: %.1f percent, number of years: %d, total amount earned: %.4f\n" % (A,p,n, sum)
