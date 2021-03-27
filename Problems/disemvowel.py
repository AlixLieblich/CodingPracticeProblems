# Trolls are attacking your comment section!

# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

# Your task is to write a function that takes a string and return a new string with all vowels removed.

# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

# Note: for this kata y isn't considered a vowel.

# def disemvowel(string):
#   #vowels=["a","e","i","o","u"]
#   for char in string:
#     print(len(string))
#     #print("start")
#     # if char == "e" or char=="i":
#       # print("!")
#       # string.pop(char)
#     string.replace('e','')
#   return string

# def disemvowel(string):
#   #str = "Engineering"
#   print ("Original string: " + str) 
#   res_str = str.replace('e', '') 
#   # removes all occurrences of 'e' 
#   print ("The string after removal of character: " + res_str) 
#   # Removing 1st occurrence of e 
#   res_str = str.replace('e', '', 1)    
#   print ("The string after removal of character: " + res_str) 
# a=disemvowel("This website is for losers LOL")
# print(a)

def disemvowel(string):
  new_string=string.replace('a', '')
  new_string=new_string.replace('e', '')
  new_string=new_string.replace('i', '')
  new_string=new_string.replace('o', '')
  new_string=new_string.replace('u', '')

  print(new_string)

disemvowel("this website is for losers lolz")