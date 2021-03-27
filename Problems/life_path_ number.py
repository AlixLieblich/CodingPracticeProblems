# A person's Life Path Number is calculated by adding each individual number in that person's date of birth, untill it is reduced to a single digit number.

# For example, Albert Einstein's birthday is March 14, 1879. The calculation of his Life Path Number would look like this:

# year: 1 + 8 + 7 + 9 = 25; 2 + 5 = 7
# month: 0 + 3 = 3
# day: 1 + 4 = 5
# final result: 7 + 3 + 5 = 15; 1 + 5 = 6
# Einstein's Life Path Number is therefore: 6

# Write the function lifePathNumber(dateOfBirth) that accepts a date of birth (as a string) on the following format: "yyyy-mm-dd". Where "y" is year, "m" is month and "d" is day. The function shall return a one digit integer between 1 and 9 which represents the Life Path Number of the given date of birth.

# You do not need to check that the input to the lifePathNumber()-function is correct format. You can assume that the input to the function will always be a valid date (as a string) with the format: "yyyy-mm-dd".

# Note: If the month or day is a single digit number, then it shall be preceeded by a 0 (zero). For example, in Einstein's case the month of March is 3; which is a single digit number. The function shall in this case be called with the following parameter: lifePathNumber("1879-03-14")


def life_path_number(birthdate):
# # # separating string into indidual integers in string 
#   string_sep=""
#   for i in birthdate:
#     string_sep+=i
  
# # seaprating string by - into list
#   string_sep=string_sep.split("-")

# # separating year month and day to be added together
#   year=[]
#   month=[]
#   day=[]
#   # for index, date in enumerate(string_sep):
#   #   # print(f"date: {date}")
#   year.append(string_sep[0])
#   month.append(string_sep[1])
#   day.append(string_sep[2])
#   print(year)
#   print(month)
#   print(day)

#   a=0
#   while len(a)>1:
#     a.split()
#     for i in year:
#       a+=i
#   return a

# # def add_em_bitchs(list):
# #   n=0

# #   for i in list:
# #     n+=i

# # to add the added date integers together
#   # n=0
#   # num=[]
#   # # for i in string_sep:
#   #   i=int(i)
#   #   n+=i
#   #   print(f"n: {n}")
#   #   num.append(n)
#   #   print(f"num: {num}")
#   # return n

  year, month, date=birthdate.split('-')
  while len(year)!=1:
    year= str(sum([int(i) for i in year]))
  while len(month) !=1:
    month=str(sum([int(i) for i in month]))
  while len(date) !=1:
    date=str(sum([int(i) for i in date]))
  total=str(int(year)+int(month)+int(date))
  while len(total) !=1:
    total=str(sum([int(i) for i in total]))
  return int(total)


print(life_path_number("1955-10-28"))