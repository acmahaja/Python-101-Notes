"Python is as simple as {0}, {1}, {2}".format("a", "b", "c")

#Output

"""
Python is as simple as a,b,c
"""

"Python is as simple as {1}, {0}, {2}".format("a", "b", "c")

#Output

"""
Python is as simple as b,a,c
"""

xy = {"x":0, "y":10}
print("Graph a point at where x={x} and y={y}".format(**xy))

#Output

"""
Graph a point at where x=0 and y=10
"""
