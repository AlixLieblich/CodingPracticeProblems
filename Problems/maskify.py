# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

# Your task is to write a function maskify, which changes all but the last four characters into '#'.

def maskify(cc):
  new_string=""
  if len(cc)>4:
    new_string += "#" * (len(cc)-4) + cc[-4:]
  return new_string  

a=(maskify("12345"))
print(a)


# this one below
def maskify(cc):
  x=cc[-4:]
  length=len(cc)
  tags=length-4
  return ("#"*tags)+x
print(maskify('1234567890'))