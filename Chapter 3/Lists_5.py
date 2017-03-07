"""
In this example, we try to assign the sorted list to a variable. However, when
you call the sort() method on a list, it sorts the list in-place. So if you try
to assign the result to another variable, then you’ll find out that you’ll get a
None object, which is like a Null in other languages. Thus when you want to sort
something, just remember that you sort them in-place and you cannot assign it to
a different variable
"""

alpha_list = [34, 23, 67, 100, 88, 2]
sorted_list = alpha_list.sort()
sorted_list
print(sorted_list)

#Output

"""
None
"""
