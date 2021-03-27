# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

# def filter_list(l):
#   lst=[]
#   for a in l:
#     a=str(a)
#     print(a)
#     if a.isnumeric:
#       lst.append(a)
#   return lst

# print(filter_list([1,2,'a','b']))


# def filter_list(l):
#   lst=[]
#   bad=[]
#   for a in l:
#     if type(a) ==type( 'i')
#       bad.append(a)
#     else:
#       lst.append(a)
#   return lst

# print(filter_list([1,2,'a','b']))

def filter_list(l):
    n=[]
    s=[]
    for i in l:
        if type(i) ==type( 'a'):
            s.append(i)
        else:
            n.append(i)
    return (n)

print(filter_list([1,2,'a','b']))