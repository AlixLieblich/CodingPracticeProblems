def nb_year(p0, percent, aug, p):
  n=0
  annual_pop=0
  percent=percent/100
  while p0<p:
    p0=p0+(p0*percent)+aug
    n+=1
  return n
print(nb_year(1500, 5, 100, 5000))