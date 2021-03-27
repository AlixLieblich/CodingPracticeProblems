#Create a function that takes a number and returns an array of strings containing the number cut off at each digit.

# def create_array_of_tiers(n):
#   if create_array_of_tiers==None:
#     return None
#   if create_array_of_tiers==[]:
#     return[]
#   n=str(n)
#   result = []
#   K=1
#   for tiers in range(0, len(n)): 
#     result+= (n[tiers : tiers + K])
#     print(result)
#     # print(type(idx))
#   return result
    
# a=create_array_of_tiers(420)
# print(a)

def create_array_of_tiers(n):
    n=str(n)
    return [n[:i] for i in range(1,len(n)+1)]
print(create_array_of_tiers(420))
