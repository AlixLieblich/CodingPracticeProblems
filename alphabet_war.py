# Introduction

# There is a war and nobody knows - the alphabet war!
# There are two groups of hostile letters. The tension between left side letters and right side letters was too high and the war began.

# Task

# Write a function that accepts fight string consists of only small letters and return who wins the fight. When the left side wins return Left side wins!, when the right side wins return Right side wins!, in other case return Let's fight again!.

# The left side letters and their power:

#  w - 4
#  p - 3
#  b - 2
#  s - 1
# The right side letters and their power:

#  m - 4
#  q - 3
#  d - 2
#  z - 1

def alphabet_war(fight):
  wcount, pcount,bcount,scount,mcount,qcount,dcount,zcount=0,0,0,0,0,0,0,0
  for letters in fight:
    for j in str(letters):
      if j=="w": wcount+=4
      elif j=="p": pcount+=3
      elif j=="b": bcount+=2
      elif j=="s": scount+=1
      elif j=="m": mcount+=4
      elif j=="q": qcount+=3
      elif j=="d": dcount+=2
      elif j=="z": zcount+=1
  left_score=wcount+bcount+scount+pcount
  print(left_score)
  rigth_score=mcount+qcount+dcount+zcount
  print(rigth_score)
  if left_score>rigth_score:
    return ("Left side wins!")
  elif rigth_score>left_score:
    return ("Right side wins!")
  elif rigth_score==left_score:
    return ("Let's fight again!")

print(alphabet_war("zdqmwpbs"))