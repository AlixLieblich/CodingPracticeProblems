def get_grade(s1, s2, s3):
  av=((s1+s2+s3)/3)
  print(av)
  if 90<=av<=100:
    grade='A'
  if 80<=av<90:
    grade='B'
  if 70<=av<80:
    grade='C'
  if 60<=av<70:
    grade='D'
  if 0<=av<60:
    grade='F'
  return grade

print(get_grade(70, 70, 100))