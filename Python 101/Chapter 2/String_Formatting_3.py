int_float_err = "%i + %f" % ("1", "2.00")

#Output

"""
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    int_float_err = "%i + %f" % ("1", "2.00")
TypeError: %i format: a number is required, not str
"""

int_float_err = "%i + %f" % (1, "2.00")

#Output

"""
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    int_float_err = "%i + %f" % (1, "2.00")
TypeError: must be real number, not str
"""
