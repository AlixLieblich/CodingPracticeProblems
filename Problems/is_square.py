# test if n is a perfect sqaure or not
import math
def is_square(n):    
  if n < 0:
    return False #check if n is negative
  l=math.sqrt(n)
  if l - (int(l))==0: # if the sqrt of n - int(n) is = 0, 
                      # then you know you have no decimals
    return True
  if l-(int(l))!=0:
    return False