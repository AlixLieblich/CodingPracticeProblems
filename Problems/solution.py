
def solution(number):
  if number<0:
    return 0
  list=[]
  i=1
  while 0<=i<number:
    list.append(i)
    i+=1
  sum=0
  for num in list:
    if (num%5==0) or (num%3==0):
      sum+=num
  return sum

print(solution(20))