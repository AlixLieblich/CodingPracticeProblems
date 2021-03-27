# NOT FULLY FINISHED
# https://www.codewars.com/kata/558878ab7591c911a4000007/train/python

# Pig Latin is an English language game where the goal is to hide the meaning of a word from people not aware of the rules.

# So, the goal of this kata is to wite a function that encodes a single word string to pig latin.

# The rules themselves are rather easy:

# The word starts with a vowel(a,e,i,o,u) -> return the original string plus "way".

# The word starts with a consonant -> move consonants from the beginning of the word to the end of the word until the first vowel, then return it plus "ay".

# The result must be lowercase, regardless of the case of the input. If the input string has any non-alpha characters, the function must return None, null, Nothing (depending on the language).

# The function must also handle simple random strings and not just English words.

# The input string has no vowels -> return the original string plus "ay".

# For example, the word "spaghetti" becomes "aghettispay" because the first two letters ("sp") are consonants, so they are moved to the end of the string and "ay" is appended.

def pig_latin(s):
  # s=s.lower()
  # for int in s:
  #   if int.isnumeric():
  #     return None
  # slist=[]
  # for let in s:
  #   slist.append(s)
  
  # first=slist[0]
  # second=slist[1]
  # last="ay"
  # x=""
  # if (first=="a") or (first=="e") or (first=="i") or (first=="o") or (first=="u"):
  #   last="way"
  #   x+= (f"{s}{last}")

  #   if first==second:
  #     x+= (f"{s}{last}") 

  #     if ((first!="a") or (first!="e") or (first!="i") or (first!="o") or (first!="u")) and ((second !="a") and (second!="e") and (second!="i") and (second!="o") and (second!="u")):
  #       s=s.replace(first,"")
  #       s=s.replace(second,"")
  #       x += (f"{s}{first}{second}{last}")

  #       if ((first!="a") and (first!="e") and (first!="i") and (first!="o") and (first!="u")) and ((second =="a") or (second=="e") or (second=="i") or (second=="o") or (second=="u")):
  #         word=s.replace(first,"")
  #         x+= (f"{word}{first}{last}") 
  # return x
  # print(x)

  # vowel=['a','e','i','o','u']
  # s=s.lower()
  # first = str(s[0])
  # second=str([1])
  # last="ay"
  # if not s.isalpha():
  #   return None
  # if s[0] in vowel:
  #     last="way"
  #     return (f"{s}{last}")
  # if s[0]==s[1]:
  #   return (f"{s}{s}{last}")
  # if s[0] not in vowel and s[1] not in vowel:
  #   print(type(s))
  #   print(type(first))
  #   s=s.replace(first,"")
  #   s=s.replace(second,"")
  #   return (f"{s}{first}{second}{last}")
  # else:
  #   word=s.replace(first,"")
  #   return (f"{word}{first}{last}") 

  vowel=['a','e','i','o','u']
  s=s.lower()
  last="ay"
  if not s.isalpha():
    return None
  if s[0] in vowel:
      last="way"
      return (f"{s}{last}")
  if s[0]==s[1]:
    return (f"{s}{last}")
  if s[0] not in vowel and s[1] not in vowel:
    s=s.replace(s[0],"")
    s=s.replace(s[1],"")
    return (f"{s}{s[0]}{s[1]}{last}")
  else:
    word=s.replace(s[0],"")
    return (f"{word}{s[0]}ay") 



print(pig_latin("hello"))
