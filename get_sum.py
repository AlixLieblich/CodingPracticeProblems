# Given two integers a and b, which can be positive or negative, find the sum of all the integers between including them too and return it. If the two numbers are equal return a or b.

# Note: a and b are not ordered!


def get_sum(a,b):
# function to add all the numbers between a and b
  if a == b:
    return a
  s = 0
  for n in range(min(a,b), max(a,b)+1):
    s+=n
  return s
l=get_sum(1,2)
print(l)