# Write your check_for_name function here:
def check_for_name(sentence, name):
  return name.lower() in sentence.lower()

# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

"""
As you can see, this function can be created using one line.
The in keyword will return True if the first provided string is within the second.
So in this case, we’re checking if name is in sentence. In order to ignore differences in capitalization, we can use the .lower() function which converts all characters to lowercase characters.
"""
