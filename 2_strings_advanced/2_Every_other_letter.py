# Write your every_other_letter function here:
def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other

# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print

"""
In order to alternate which character is added to the every_other string, we use a range of indices which starts at index 0 (the beginning of our word) and ends at the end of our word.
The third parameter in the range function determines what value to increment by.
In this case, we want to increment by 2 in order to get every other letter.

Another way to loop through all indices of our original string, but only add the letters that correspond to an even index.
As a challenge, try solving this problem that way!
"""
