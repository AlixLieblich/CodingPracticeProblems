# Story

# You and a group of friends are earning some extra money in the school holidays by re-painting the numbers on people's letterboxes for a small fee.

# Since there are 10 of you in the group each person just concentrates on painting one digit! For example, somebody will paint only the 1's, somebody else will paint only the 2's and so on...

# But at the end of the day you realise not everybody did the same amount of work.

# To avoid any fights you need to distribute the money fairly. That's where this Kata comes in.

# Kata Task

# Given the start and end letterbox numbers, write a method to return the frequency of all 10 digits painted.

# Example

# For start = 125, and end = 132

# The letterboxes are

# 125 = 1, 2, 5
# 126 = 1, 2, 6
# 127 = 1, 2, 7
# 128 = 1, 2, 8
# 129 = 1, 2, 9
# 130 = 1, 3, 0
# 131 = 1, 3, 1
# 132 = 1, 3, 2
# The digit frequencies are:

# 0 is painted 1 time
# 1 is painted 9 times
# 2 is painted 6 times
# etc...
# and so the method would return [1,9,6,3,0,1,1,1,1,1]


##code that didnt work
# def paint_letterboxes(start, finish):
#   box_range=range(start, finish+1)
#   box_list=list(box_range)
#   print(box_list)
#   string=[]
#   for i in box_list:
#     i=str(i)
#     string+=i
#   print(string)

#   occurences=[]
#   n=0
#   l=0
#   while l <10:
#     for i in string:
#       if i == l:
#         print(f"i: {i}")
#       print(f"l: {l}")
#       n+=1
#       occurences.append(n)
#       l+=1
#   return occurences

def paint_letterboxes(start, finish):
  count0,count1,count2,count3,count4,count5,count6,count7,count8,count9=0,0,0,0,0,0,0,0,0,0
  for i in range(start, finish+1):
    for j in str(i):
      if j =="0":count0+=1
      elif j=="1": count1+=1
      elif j=="2": count2+=2
      elif j == '3': count3 += 1
      elif j == '4': count4 += 1
      elif j == '5': count5 += 1
      elif j == '6': count6 += 1
      elif j == '7': count7 += 1
      elif j == '8': count8 += 1
      else: count9 += 1     
  return [count0,count1,count2,count3,count4,count5,count6,count7,count8,count9]
    


print(paint_letterboxes(125,132))