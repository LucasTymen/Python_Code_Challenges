# Write your count_first_letter function here:
def count_first_letter(names):
  letters = {}
  for key in names:
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters

# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}

"""
This function uses two dictionaries instead of one dictionary and one list.
We iterate through each of the keys (which are the last names) and store the first letter of the last name in first_letter.
We then use similar logic to what we have used before by testing if we have already seen that letter before.
If we haven’t seen that letter before, then we add it to our dictionary with a value of 0.
Next, we are going to increment the value.
Since we know that some people share the last name (as seen by the list of first names in our names dictionary), we are going to increment the
value in our letters dictionary by the length of first names that share the last name for our current iteration (key).
"""
