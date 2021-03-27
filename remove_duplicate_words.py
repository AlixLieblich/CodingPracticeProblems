def remove_duplicate_words(s):
  print()
  old=[]
  new=[]
  new=s.split()
  for y in new:
    if y not in old:
      old.append(y)
  strng=" "
  here=strng.join(old)
  return here
  # return(strng)
# print(remove_duplicate_words("my cat is my cat fat"))
remove_duplicate_words("my cat is my cat fat")