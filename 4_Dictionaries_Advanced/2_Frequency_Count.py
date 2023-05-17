# Write your frequency_dictionary function here:
def frequency_dictionary(words):
  my_storage = {}
  for word in words:
    if word not in my_storage:
      my_storage[word] =+ 0
    my_storage[word] =+ 1
  return my_storage

# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

"""
To create a new dictionary we set a variable equal to {}.
We iterate through each of the strings in the list of strings and check if it is already in our dictionary using the in keyword.
If it is not then we add it as a new key-value pair where the value is 0.
Regardless of whether the string was already in the dictionary, increase the value by 1.
This will make it so all new entries will have a value of 1 and all existing entries will increase their old value by 1.
"""
