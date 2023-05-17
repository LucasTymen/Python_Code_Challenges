# Write your reverse_string function here:
def reverse_string(word):
  txt = word [::-1]
  return txt

# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

# ===========>>>>>> solution
def reverse_string(word):
  reverse = ""
  for i in range(len(word)-1, -1, -1):
    reverse += word[i]
  return reverse

"""
This is similar to the last solution, but our range has been modified in order to start at the last index of the string (length of the string minus one) up to the first index.
Since the parameter for the ending index is exclusive we need to provide the index of one more iteration than what we want to stop at.
We want to stop at 0, and since we are incrementing by -1, we will set the ending index to -1.
Finally, make sure to add the third parameter of -1. This makes us increment by -1 at each step.
"""
