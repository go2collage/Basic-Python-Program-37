# Combine two Dictionary adding values for common keys

# d1 = {'a': 100, 'b':200, 'c':300}
# d2 = {'a': 300, 'b':200, 'd':400}

# import lib
from collections import Counter
# Dictionary 
d1 = {'a': 100, 'b':200, 'c':300}
d2 = {'a': 300, 'b':200, 'd':400}

print("Dictionary 1 is: ", d1)
print("Dictionary 2 is: ", d2)

# combine two dictionary
d3 = Counter(d1) + Counter(d2)

print("After combine and adding values, Dictionary 3 is: ", d3)

# Thanks for Watching
