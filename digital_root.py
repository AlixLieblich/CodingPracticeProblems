# def digital_root(n):
#     n=str(n)
#     n.split()
#     print(n)
#     root=""
#     print("ghehrg")
#     while len(root)>1:
#         print("ere")
#         for inte in n:
#             inte=int(inte)
#             root+=inte
#             print(root)
#     return root

# print(digital_root(942))

# def digital_root(n):
#   n=str(n)
#   n.split()
#   root=""
#   i=0
#   while len(i)>=1:
#     print("ji")
#     for inte in n:
#       print(inte)
#       root+=inte
#       print(root)
#       i+=1
#   return root

# digital_root(16)

# def digital_root(n):
#   if n ==None:
#     return None
#   n=str(n)
#   lst=[]
#   for m in n:
#     lst.append(m)
#   root="10"

#   while len(root)>=2:
#     for num in lst:
#       root=int(root)
#       num=int(num)
#       root+=num
#       # root=str(root)
#     # root=root
#     return root-10
#   root-=10
      
#   return root



# print(digital_root(1622))


# def digital_root(n):
#   if n ==None:
#     return None
#   n=str(n)
#   lst=[]
#   for m in n:
#     lst.append(m)
#   print(lst)
#   new_lst=lst
#   while len(new_lst)>2:
#     for num in new_lst:
#       root+=num
#       root=str(root)
#       print(root)
      
#   return root



# digital_root(1622)

# def digital_root(n):
#   if n ==None:
#     return None
#   n=str(n)
#   lst=[]
#   for m in n:
#     lst.append(m)
#   root=0
#   for num in lst:
#     num=int(num)
#     root+=num
#     print(root)
#     # root=str(root)
#     root=str(root)
#     if len(root)<2:
#       return root
#     # root=int(root)
      
#   return root



# digital_root(1622)

# def digital_root(n):
#   if n ==None:
#     return None
#   n=str(n)
#   lst=[]
#   for m in n:
#     lst.append(m)
#   root=0
#   new_lst=[]
#   for num in lst:
#     num=int(num)
#     root+=num
#     new_lst.append(root)
#   print(new_lst)
#   x=new_lst[-1]
#   if len(x)>2:
    
#   return root



# digital_root(1622)

# def break_up(lst):
#   root=0
#   new_lst=[]
#   for num in lst:
#     num=int(num)
#     root+=num
#     new_lst.append(root)

# def digital_root(n):
#   if n ==None:
#     return None
#   n=str(n)
#   lst=[]
#   for m in n:
#     lst.append(m)
#   break_up(lst)
#   x=lst[-1]
#   if len(x)>2:
#     break_up(lst)
#   return lst



# print(digital_root(1622))



def digital_root(n):
  lst=[]
  n=str(n)
  for m in n:
    m=int(m)
    lst.append(m)
  summ=sum(lst)
  summ=str(summ)
  new_list=[]
  while (len(summ))>1:
    for num in summ:
      num=int(num)
      new_list.append(num)
    summ=sum(new_list)
    summ=str(summ)
  print(summ)
  return summ

digital_root(132189)