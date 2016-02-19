
"""
File: <Sin2_plus_cos2>

Copyright (c) 2016 <Lauren Graziani>

License: MIT

<debugging a program>
"""




"""
# a
from math import sin, cos #need to import pi from math
x = pi/4
1_val = math.sin^2(x) + math.cos^2(x) #can't start a variable with a number, powers are written by **
print 1_VAL
"""
# a debugged
from math import sin, cos, pi
x = pi / 4
val1 = sin(x) ** 2 + cos(x) ** 2
print val1

"""
# b
v0 = 3 m/s  #get rid of m/s
t = 1 s     #get rid of s
a = 2 m/s**2      # **2 should come right after 2, get rid of m/s
s = v0.t + 0,5.a.t**2 #v0.t should be v0*2, change comma to period and periods to *
print s
"""
# b debugged
v0 = 3
t = 1
a = 2 ** 2
s = v0*t + 0.5*a*t**2
print s
#c
"""
a = 3,3 b = 5,3
a2 = a**2
b2 = b**2
eq1_sum = a2 + 2ab + b2
eq2_sum = a2 - (2ab + b2
eq1_pow = (a+b)**2
eq2_pow = (a-b)**2
print 'First equation: %g = %g',  % (eq1_sum, eq1_pow)
print 'Second equation: %h = %h', % (eq2_pow, eq2_pow)

# c debugged (cofused???)
a = 3,3
b=5,3
a2 = a**2
b2 = b**2
eq1_sum = a2 + (2*a*b) + b2
eq2_sum = a2 - (2*a*b) + b2
eq1_pow = (a+b)**2
eq2_pow = (a-b)**2
print "First equation: %g = %g"  % (eq1_sum, eq1_pow)
print "Second equation: %h = %h" % (eq2_pow, eq2_pow)
"""
