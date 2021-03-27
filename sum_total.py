
def sum_total(numbers):
  ### a function to take in a list and return the sum of integers therein
  strng=0
  for num in numbers:
    strng+=num
  return strng
print(sum_total([1,10,1]))