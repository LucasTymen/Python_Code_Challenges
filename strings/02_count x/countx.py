# Write your count_char_x function here:
def count_char_x(word,x):
  counter = 0
  for x in word.split(x):
    counter += 1
  return counter -1

# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

# ===========>>>>>> solution
def count_char_x(word, x):
  occurrences = 0
  for letter in word:
    if letter == x:
      occurrences += 1
  return occurrences
