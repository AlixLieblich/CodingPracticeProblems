# This time no story, no theory. The examples below show you how to write function accum:

# Examples:

# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(s):
  print()
  strng=""
  i=0
  for a in s:
    a=a.lower()
    strng+=a.upper()
    strng+=(a*i)
    i+=1
    strng+="-"
  strng=strng[:-1]
  return strng
print(accum("ZpglnRxqenU"))

