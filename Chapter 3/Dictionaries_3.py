my_dict = {"name":"Mike", "address":"123 Happy Way"}

my_dict.keys()

#Output
"""
dict_keys(['name', 'address'])
"""

"""
In Python 2, the keys method returns a list. But in Python 3, it returns a view
object. This gives the developer the ability to update the dictionary and the
view will automatically update too. Also note that when using the in keyword
for dictionary membership testing, it is better to do it against the
dictionary instead of the list returned from the keys method. See below:
"""

"name" in my_dict               # this is good
"name" in my_dict.keys()        # this works too, but is slower
