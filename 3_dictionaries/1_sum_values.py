# Write your sum_values function here:
# Write your sum_values function here:
def sum_values(my_dictionary):
  counter = 0
  for value in my_dictionary.values():
    counter += value
  return counter

# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6
# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

"""
We start by creating a variable to keep track of the total.
Next, we use the values() function in our for loop in order to iterate through each of the values in the dictionary.
Using this, we can access each value and add it to our total variable. At the end of our loop, we return the total.
"""
