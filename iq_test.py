# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

# ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

def iq_test(numbers):

## create a function which takes a list and determines if there is an outlying number which is either even or odd; then print a statement saying where in the list of numbers the outlier is

  # convert list of string to list of int
  numbers_list=[]
  new_numbers=numbers.split(" ")
  for val in new_numbers:
    val=int(val)
    numbers_list.append(val)

  # create two var and two lists
  even=0
  even_num=[]
  odd=0
  odd_num=[]

  # determine if even or odd; if even, add 1 to even var and append num to even list; if odd, add 1 to odd var and append num to odd list
  for num in numbers_list:
    if num%2==0:
      even+=1
      even_num.append(num)
    if num%2!=0:
      odd+=1
      odd_num.append(num)

  # if the odd var is equal to one, the outlier of the list is odd; set the outlier var to said number
  if odd ==1:
    for outliers in odd_num:
      outlier=outliers
  if odd==1:
    condition="odd"
    not_condition="even"
    for i, number in enumerate(numbers_list):
      if number == outlier:
        index=i

  if even==1:
    condition="even"
    not_condition="odd"
    for i, number in enumerate(numbers_list):
      if number == outlier:
        index=i

 # convert index positions to their corresponding english word
  if index==0:
    index_english="First"
  if index==1:
    index_english="Second"
  if index==2:
    index_english="Third"
  if index_english==3:
    index_english="Fourth"
  if index==4:
    index_english="Fifth"
  print(index+1)
  print(f"{index_english} number is {condition}, while the rest of the numbers are {not_condition}")

iq_test('2 4 7 8 10')