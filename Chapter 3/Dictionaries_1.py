"""
A Python dictionary is basically a hash table or a hash mapping. In some
languages, they might be referred to as associative memories or associative
arrays. They are indexed with keys, which can be any immutable type.

For example, a string or number can be a key. You need to be aware that a
dictionary is an unordered set of key:value pairs and the keys must be unique.
You can get a list of keys by calling a dictionary instance’s keys method.

To check if a dictionary has a key, you can use Python’s in keyword. In some of
the older versions of Python (2.3 and older to be specific), you will see the
has_key keyword used for testing if a key is in a dictionary. This keyword is
deprecated in Python 2.x and removed entirely from Python 3.x.

Let’s take a moment to see how we create a dictionary.
"""

my_dict = {}
another_dict = dict()
my_other_dict = {"one":1, "two":2, "three":3}
my_other_dict

#Output
"""
{'one': 1, 'two': 2, 'three': 3}
"""

my_other_dict =["one"]

#Output
"""
1
"""

my_dict = {"name":"Mike", "address":"123 Happy Way"}
my_dict["name"]

#Output
"""
'Mike'
"""
