def more(numbers):
  ### function that returns wether a list has more even or odd integers
  even=0
  odd=0
  for num in numbers:
    if (num%2==0):
      even +=1
    if (num%2!=0):
      odd+=1
  if even>odd:
    return 'even'
  if odd>even:
    return 'odd'
  if odd==even:
    return 'its a tie'

print(more([1,2,3,4,6]))