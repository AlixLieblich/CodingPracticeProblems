# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

def get_count(input_str):
    num_vowels = 0
    for letters in input_str:
      if letters == "a" or letters =="e"or letters =="i" or letters =="o" or letters =="u":
        num_vowels+=1
    return num_vowels
print(get_count("abracadabra"))


#newer quicker solution:
def get_count(input_str):
  num_vowels = 0
  vowels=['a','e','i','o','u']
  for letters in input_str:
    if letters in vowels:
      num_vowels+=1

  return num_vowels