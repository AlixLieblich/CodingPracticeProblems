
def xo(s):
  s=s.lower()
  x, o = 0, 0
  for let in s:
    if let == "x": x+=1
    if let == "o": o+=1
  if x==o:
    return True
  else:
    return False
print(xo('xoxo'))