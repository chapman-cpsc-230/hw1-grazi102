
"""
File: <Seconds2years.py>

Copyright (c) 2016 <Lauren Graziani>

License: MIT

<Converting seconds to years>
"""


seconds = raw_input ('Type number of seconds to be converted to years\n')
years = float(seconds) / (365.2425 * 24 * 60 * 60)
print "%s seconds equals %.2f years" % (seconds, years)
if years <= 82: #average lifetime of person from Norway
    print "Yes, a child in Norway would be expected to live more than %s seconds which equals %.2f years.\n" % (seconds, years)
else:
    print "No, a child in Norway would not be expected to live more than %s seconds which equals %.2f years.\n" % (seconds, years)
