# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
  counter = 0
  for key in my_dictionary.keys():
    if key % 2 == 0:
      counter += my_dictionary[key]
  return counter

# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

"""
Similar to the previous problem, we are iterating through our dictionary, except this time we are iterating through the keys instead of the values.
In order to get the keys we use the keys() function and to get the value of a key we can use brackets.
To test if the key is even we use the modulus operator and test if the remainder is 0 when dividing by 2.
"""
