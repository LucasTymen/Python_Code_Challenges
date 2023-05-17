# Write your add_ten function here:
def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  return my_dictionary

# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}


"""
We use a for loop to iterate through each key and we access the value using the key.
After accessing it, we overwrite the value with the value plus 10. Finally, we return the modified dictionary.
"""
