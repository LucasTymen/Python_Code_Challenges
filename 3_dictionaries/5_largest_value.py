def max_key(my_dictionary):
  largest_key = float("-inf")
  largest_value = float("-inf")
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key

# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"


"""
In order to program the max algorithm using dictionaries, we need to keep track of the max value and the key which is used to access it.
We start by using float("-inf") in order to initialize them to the lowest possible value.
To retrieve the key and value at the same time, we use the items() function.
Inside our loop, we overwrite the current largest value and the key used to access whenever we find a larger value.
We return the largest value’s key once we have iterated through the entire dictionary.
"""
