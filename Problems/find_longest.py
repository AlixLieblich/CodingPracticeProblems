def find_longest(words):
  longest_word=""
  for word in words:
    if len(word)>len(longest_word):
      longest_word=""
      longest_word+=word
  return longest_word
print(find_longest(['one', 'two', 'superduper', 'dog'] ))