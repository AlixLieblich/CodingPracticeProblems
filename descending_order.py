# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

# Examples:

# Input: 42145 Output: 54421

# Input: 145263 Output: 654321

# Input: 123456789 Output: 987654321


def descending_order(num):
  num=str(num) # convert num (type int) to string
  lst=[] # create empty list
  for i in num:
    lst.append(i) # add indv characters from string to list
  lst.sort() # sort the list high to low
  lst=lst[::-1] # flip the list backwards
  s="" # create empty string 
  strng=int(s.join(lst)) # join the list characters together in the string and covert to int
  return strng # return value stored in strng

