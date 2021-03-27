# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

def find_outlier(integers):
  even=0
  even_num=[]
  odd=0
  odd_num=[]
  for integer in integers:
    if integer%2==0:
      even+=1
      even_num.append(integer)
    if integer%2!=0:
      odd+=1
      odd_num.append(integer)
  if even==1:
    condition="even"
    for num in even_num:
      N=num
  if odd==1:
    condition="odd"
    for num in odd_num:
      N=num
  return None

  print(f"Should return {N} the only {condition} number.")




find_outlier([160, 3, 1719, 19, 11, 13, -21])