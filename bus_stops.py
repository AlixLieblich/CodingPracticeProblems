def number(bus_stops):
  total1, total2=0,0
  for stops, i in enumerate(bus_stops):
    total1+=(bus_stops[stops][0])
    total2+=(bus_stops[stops][1])
  return max(total1,total2)-min(total1,total2)
print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))