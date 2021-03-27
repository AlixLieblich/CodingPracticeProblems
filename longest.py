# Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

def longest(a1, a2):
  new="" # make a string
  lst=[] # make a list
  lst2=[] # make a list
  final="" # make a string
  new+=a1 # add both a1 and a2 to first string
  new+=a2
  for a in new:
    lst.append(a) # put a1 and a2 into a list
  lst.sort() # put list in alpha order
  for a in lst:
    if a not in lst2: # if letter not in lst2, add
      lst2.append(a)
  for a in lst2:
    final+=a # convert list to string

  return final
print(longest("aretheyhere", "yestheyarehere"))