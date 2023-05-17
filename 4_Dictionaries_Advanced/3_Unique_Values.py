# Write your unique_values function here:
def unique_values(my_dictionary):
  seen_values = []
  for value in my_dictionary.values():
    if value not in seen_values:
      seen_values.append(value)
  return len(seen_values)

# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1


"""
This function has a similar structure to the last one except that the input has been changed to a dictionary.
We iterate through each of the values and whenever we find one we have not added to our list already, we add it to the list.
After the loop, we return the length of the list since that contains all unique values from the dictionary.
"""
