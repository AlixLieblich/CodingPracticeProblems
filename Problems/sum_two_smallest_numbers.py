# def sum_two_smallest_numbers(numbers):
#   low=0
#   for num in numbers:
#     if num<low:
#       low+=num
  
#   return num
  
# print(sum_two_smallest_numbers([5, 8, 12, 18, 22,2]))


# def sum_two_smallest_numbers(numbers):
#   lowest=0
#   for num in numbers:
#     if num<lowest:
#       lowest+=num
#   low=0+num
#   for numb in numbers:
#     if numb<low:
#       low+=numb
#   print(numb)
#   return low
  
# print(sum_two_smallest_numbers([5, 8, 12, 18, 22,2]))



def sum_two_smallest_numbers(numbers):
  smol=0
  for num in numbers:
    if num<smol:
      smol+=num
  return smol

print(sum_two_smallest_numbers([5, 8, 12, 18, 22,2]))