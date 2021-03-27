def is_valid_walk(walk):
  vertical=0
  horizontal=0
  starting_point=0
  num_n=walk.count('n')
  num_e=walk.count('e')
  num_s=walk.count('s')
  num_w=walk.count('w')  
  for movement in walk:
    if movement== "n":
      vertical+=1
      starting_point+=1
    if movement== "e":
      horizontal+=1 
      starting_point+=1
    if movement== "s":
      vertical-=1 
      starting_point-=1   
    if movement== "w":
      vertical-=1
      starting_point-=1
  vert_disp=(max(num_n, num_s)-min(num_n,num_s))
  horz_disp=(max(num_w, num_e)-min(num_w,num_e))
  print(f"len walk: {len(walk)}")
  print(starting_point)
  print(f"vertical: {vertical}")
  print(horizontal)
  print(vert_disp)
  print(horz_disp)
  if (len(walk)==10) and (starting_point==0) and (vertical==0) and (horizontal==0) and (vert_disp==0) and (horz_disp==0):
    return True
  if (len(walk)==10) and (starting_point==0) and (vertical + horizontal ==0)and (vert_disp==0) and (horz_disp==0):
    return True
  elif (len(walk)!=10)or (starting_point!=0) or (vertical!=0) or (horizontal!=0)or (vert_disp!=0) or (horz_disp!=0):
    return False
