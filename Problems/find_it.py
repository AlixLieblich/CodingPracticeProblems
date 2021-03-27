def find_it(seq):
  for num in seq:
    occur=seq.count(num)
    print(occur, num)
    if (occur%2!=0):
      return num
print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))