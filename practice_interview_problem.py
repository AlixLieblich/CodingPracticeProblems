
# def add_multiples(numbers):
#   total=0
#   for i, num in enumerate(numbers):
#     if num==(numbers(i+1)):
#       print("hi")
#       total+=num


# print(add_multiples([4,4,5,6,7]))


# def add_multiples(numbers):
#   j=0
#   for num in numbers:
#     if num=num
#       j+=1


# print(add_multiples([4,4,5,6,7]))

def add_multiples(numbers):
  i=0
  total=0
  while i<len(numbers)-1:
    if numbers[i]==numbers[i+1]:
      total+=numbers[i]*2
    i+=1

  return total



print(add_multiples([4,4,5,5,6,7]))

# def add_multiples(numbers):
#   i=0
#   total=0
#   for num in numbers: # get rid of num

#   # get rid of extra check -> two fewer lines of code
#     for i<len(numbers):
#     if numbers[i]==numbers[i+1]:
#       total+=numbers[i]*2
#     i+=1

#   return total



# print(add_multiples([4,4,5,6,7]))


def add_multiples(numbers):
  i=0
  total=0
  for i, num in enumerate(numbers): # get rid of num
    if numbers[i]==numbers[i+1]:
      total+=numbers[i]*2
    i+=1

  return total