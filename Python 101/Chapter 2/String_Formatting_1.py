my_string = "I like %s" % "Python"
my_string
#Output
# 'I like Python'

var = "cookies"
newString = "I like %s" % var
newString
#Output
# 'I like cookies'

another_string = "I like %s and %s" % ("Python", var)
another_string
#Output
# I like Python and cookies


another_string = "I like %s and %s" % "Python"
#Output

"""
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    another_string = "I like %s and %s" % "Python"
TypeError: not enough arguments for format string
"""
