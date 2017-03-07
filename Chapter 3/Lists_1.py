"""
A Python list is similar to an array in other languages. In Python, an empty
list can be created in the following ways
"""

my_list = []
my_list = list()

"""
As you can see, you can create the list using square brackets or by using the
Python built-in, list. A list contains a list of elements, such as strings,
integers, objects or a mixture of types. Let’s take a look at some examples:
"""
my_list = [1,2,3]
my_list2 = ["a", "b", "c"]
my_list3 = ["a", 1, "Python", 5]

"""
The first list has 3 integers, the second has 3 strings and the third has a
mixture. You can also create lists of lists like this:
"""
"""
A nested list is simply a list that occurs as an element of another list
(which may of course itself be an element of another list, etc.). Common reasons
nested lists arise are: They're matrices (a list of rows, where each row is
itself a list, or a list of columns where each column is itself a list).

"""
my_nested_list = [my_list, my_list2]
my_nested_list

#Output

"""
[[1, 2, 3], ['a', 'b', 'c']]
"""
