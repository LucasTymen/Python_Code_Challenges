# Write your word_length_dictionary function here:
def word_length_dictionary(words):
  wordlength = {}
  for word in words:
    wordlength[word] = len(word)
  return wordlength

# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}


"""
To create a new dictionary we set a variable equal to {}.
While iterating through each string in our string list, we can add the key and value to our dictionary using this syntax: word_lengths[word] = len(word).
"""
