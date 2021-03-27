# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

#https://github.com/monajalal/Python_Playground/blob/master/unique_in_order.py (proper answer)

def unique_in_order(iterable):
  # convert string to list
  list1=[]
  K=1
  for idx in range(0, len(iterable)):
    list1 += iterable[idx : idx +K]
  for char, i in enumerate(list1):
    a=i-1
    print(a)
  # string=""
  # for char, i in enumerate(list1):
  #   print(char([i]-1))
  #   if char!= (char([i]-1)):
  #     print(char([i]-1))
  #     string+=char
  #     print(string)
  # return string
      

print(unique_in_order('AAAABBBCCDAABBB'))