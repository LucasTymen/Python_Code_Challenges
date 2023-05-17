# Write your make_spoonerism function here:
def make_spoonerism(word1,word2):
  return word1.replace(word1[0],word2[0]) + " " + word2.replace(word2[0],word1[0])

# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a

# ===========>>>>>> CodeCademy solution <<<<<===========
def make_spoonerism(word1, word2):
  return word2[0]+word1[1:]+" "+word1[0]+word2[1:]

"""
We can accomplish the task in one line by appending and slicing at the same time.
We can get the first index of our words by using word1[0] and word2[0] which gets the letter at the first index.
In order to get the remaining letters we can use word1[1:] and word2[1:].
This returns all characters in the strings starting with index 1 and on. We concatenate everything together to get the result.
"""
