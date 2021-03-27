def get_vowels(words):
  vowels=['a','e','i','o','u']
  vowel_words=[]
  for word in words:
    if word[0] in vowels:
      vowel_words.append(word)
  return vowel_words

print(get_vowels(['elephant','hello','octopus','greg','zebra','egg']))