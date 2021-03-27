# def db_sort(arr): 
#   print()
#   print()
#   # alpha=[]
#   num=[]
#   # for a in arr:
#   counter=0
#   while counter<len(arr):
#     for a in arr:
#       a=str(a)
#       if a.isnumeric():
#         print(a)
#         num.append(a)
#         print(num)
#       num=num.sort()
#       print(num)
#   counter+=1
# print(db_sort([6, 2, 3, 4, 5]))


    # if a.isalpha():
    #   # alpha+=a
    #   alpha.append(a)
    # # alpha=alpha.sort()

# def db_sort(arr): 
#   print()
#   print()
#   alpha, num=[], []
  
#   for a in arr:
#     a=str(a)
#     if (a.isalpha()==True):
#       print(a)
#       alpha.append(a)
#       alpha.sort()
#     print(alpha)
#   for a in arr:
#     a=int(a)
#     if (a.isalum==True):
#       if (a.isnumeric==True):
#         print(a)
#         num.append(a)
#         num.sort()
#       print("num:")
#       print(num)
# print(db_sort(["Banana", "Orange", "Apple", "Mango", 0, 2, 2]))



def db_sort(arr): 
  print()
  print()
  alpha, num=[], []
  
  for a in arr:
    if type(a)==int:
      a=int(a)
      num.append(a)
      print(num)
      # for let in a:
      #   if let.isalpha ==True:
      #     alpha.append(a)
    else:
      alpha.append(a)
  print("return:")
  return sorted(num)+sorted(alpha)
print(db_sort(["Apple",46,"287",574,"Peach","3","69",78,"Grape","423"]))