# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

# If you want to know more http://en.wikipedia.org/wiki/DNA

# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

def DNA_strand(dna):
  dna=dna.upper()
  compStrand=[]
  #string=""
  for r in (dna):
    if r =="A":
      result="T"
      compStrand.append(result)
    if r=="G":
      result="C"
      compStrand.append(result)
    if r=="T":
      result="A"
      compStrand.append(result)
    if r== "C":
      result="G"
      compStrand.append(result)
    string = ''.join([str(elem) for elem in compStrand]) 

  print(f"The complementary strand for {dna} is {string}.")

DNA_strand("AGCTagtc")
    
def DNA_strand(dna):
  dna=dna.upper()
  comp_strand=""
  for r in dna:
    print(r)
    if r == "A":
      comp_strand+="T"
    if r == "T": 
      comp_strand+="A"
    if r == "G": 
      comp_strand+="C"
    if r == "C":
      comp_strand+="G"
  return comp_strand

print(DNA_strand("AAAA"))