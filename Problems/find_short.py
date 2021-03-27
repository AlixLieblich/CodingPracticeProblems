#print the shortest word in a string

def find_short(s):
  lenlist=[]
  list=s.split()
  for i in list:
    lenlist.append(len(i))
  return min(lenlist)

print(find_short("bitcoin take over the world maybe who knows perhaps"))
