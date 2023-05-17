# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
  my_list =[]
  for value in my_dictionary.values():
    if value in my_dictionary:
      my_list.append(value)
  return my_list

# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

"""
For this solution, we iterate through every value within the dictionary.
In order to check if it is also a key, we can use the in keyword.
This checks the value against all of the keys in the dictionary to see if it exists as a key as well.
If it does, then we append it to our list of values which are also keys.
"""
