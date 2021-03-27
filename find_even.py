def find_even(numbers):
  locations=[]
  for i, num in enumerate(numbers):
    if (num%2)==0:
      a=numbers.index(num)
      locations.append(a)
  return locations
print(find_even([2, 5, 3, 4,5,6,7,8,9,10]))

def find_even(numbers):
  even_locations=[]
  for num in numbers:
    if (num%2==0):
      var=numbers.index(num)
      even_locations.append(var)
  return even_locations

print(find_even([1,2,3,4,5,6,6]))