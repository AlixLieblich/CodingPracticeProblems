
def odd_or_even(arr):
  summ=sum(arr)
  if (summ % 2)==0:
    return "even"
  else:
    return "odd"

print(odd_or_even([0, 1, 3]))