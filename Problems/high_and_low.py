# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

# Example:

# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"

def high_and_low(numbers):
  for num in numbers:
    high= max(num)
    low=min(num)
    var= (high, low)

    return var
print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
  


# 1
# def high_and_low(numbers):
#     numbers=numbers.split()
#     print()
#     print()
#     print(numbers)
#     # for i in numbers:
#       # high=max(i)
#       # low=min(i)
#     print(min(numbers))
#     print(max(numbers))
#     # var = (f"here {high} {low}")
    
#     # return var
# print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))

# 2
# def high_and_low(numbers):
#   numbers=numbers.split()
#   print()
#   print()
#   print(numbers)
#   for num in numbers:
#     num=int(num)
#   numbers=sorted(numbers)
#   print(numbers)
#   return (min(numbers))
#   return (max(numbers))
# print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))


# 3
# def high_and_low(numbers):
#   print()
#   print()
#   print()
#   print()
#   numbers=numbers.split()
#   string_int=""
#   for num in numbers:
#     string_int+=num
#     num=int(num)
#     string_int+=" "
#     print(type(num))
#   print("orig:")
#   print(string_int)
#   string_int=sorted(string_int)
#   print("sorted: ")
#   print(string_int)

# print(high_and_low("4 5 29 54 4 0 542 1 6"))

#4 (with solutions help)
def high_and_low(numbers):
  print()
  print()
  print()
  print()
  numbers=numbers.split()
  i=0
  highest =int(numbers[0])
  lowest=int(numbers[0])
  while i <len(numbers):
    numbers[i]=int(numbers[i])
    if numbers[i] > highest:
      highest = numbers[i]
    if numbers[i] < lowest:
      lowest = numbers[i]
    i+=1
  highest= str(highest)
  lowest=str(lowest)
  return highest+" "+lowest



print(high_and_low("4 5 29 54 4 0 542 1 6"))

def high_and_low(numbers):
    numlist = numbers.split(" ")
    i = 0
    highest = int(numlist[0])
    lowest = int(numlist[0])
    while i < len(numlist):
        numlist[i] = int(numlist[i])
        if numlist[i] > highest:
            highest = numlist[i]
        if numlist[i] < lowest:
            lowest = numlist[i]
        i += 1
    highest = str(highest)
    lowest = str(lowest)
    return  highest+" "+lowest
print(high_and_low("4 5 29 54 4 0 542 1 6"))
