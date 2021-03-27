#return the middlemost or two middlemost characters in a string

def get_middle(s):
  length=len(s)
  half=(length/2)
  strng=str(s)
  if int(half)-half!=0:
    half=int(half)
    return (strng[half])
  if int(half)-half==0:
    first=int(half+0.5)
    second=int(half-0.5)
    return (strng[second])+(strng[first]) 

print(get_middle("test"))