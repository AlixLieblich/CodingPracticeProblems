def order_weight(strng):
  print(strng)
  print(type(strng))
  string=strng.split(" ")
  # return string
  print(string)
  print(type(string))


  new_string=""
  K=1
  for weights in range (0, len(string)):
    weights=str(weights)
    print(f"weights: {weights}")
    print(type(weights))
    new_string+= (string[weights:weights+K])
    new_string+= ", "
    return new_string

def add_each():
  num=""
  for numbers in list:
    numbers.split()
    num+=numbers
    print(num)
    # for integers in num:



# print(order_weight("103 123 4444 99 2000"))