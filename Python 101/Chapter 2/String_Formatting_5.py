print("%(value)s %(value)s %(value)s") % {"value":"SPAM"}

#Output

"""
SPAM SPAM SPAM
"""

print("%(x)i + %(y)i = %(z)i") % {"x":1, "y":2}

#Output

"""
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print("%(x)i + %(y)i = %(z)i") % {"x":1, "y":2}
TypeError: unsupported operand type(s) for %: 'NoneType' and 'dict'
"""

print("%(x)i + %(y)i = %(z)i") % {"x":1, "y":2, "z":3}

#Output

"""
1 + 2 = 3
"""
