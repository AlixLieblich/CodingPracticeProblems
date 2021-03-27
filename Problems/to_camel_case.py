# def to_camel_case(text):
#   if text== None:
#       return 'An empty string was provided but not returned'
#   text=text.title()
#   if "-" in text:
#     text=text.split("-")
#   elif "_" in text:
#     text=text.split("_")
#   text=''.join(text)
#   a=text[0].lower()
#   new_text=text.replace(text[0],a)

#   return new_text

# print(to_camel_case('The-Stealth-Warrior'))

# def to_camel_case(text):
#   capitol=['A','B','C','D','E','F','G','H','I','K','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#   if text=='':
#     return ''

#   if text[0] not in capitol:
#     text=text.title()
#     if "-" in text:
#       text=text.split("-")
#     elif "_" in text:
#       text=text.split("_")
#     a=text[0].lower()
#     text="".join(text)
#     text=text.replace(text[0:3], a)


#     a=text[0].lower()
#     text="".join(text)
#     text=text.replace(text[0:3], a)
#     if "-" in text:
#       text=text.split("-")
#     elif "_" in text:
#       text=text.split("_")
#     text="".join(text)

#   return text

# print(to_camel_case('the_stealth_warrior'))

# def to_camel_case(text):
#   capitol=['A','B','C','D','E','F','G','H','I','K','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#   if text=='':
#     return ''

#   if text[0] not in capitol:
#     text=text.title()
#     if "-" and "_" in text:
#       text=text.split("-" and "_")
#       text="".join(text)
#     elif "-" in text:
#       text=text.split("-")
#     elif "_" in text:
#       text=text.split("_")
#       text="".join(text)
#     a=text[0].lower()
#     text="".join(text)
#     text=text.replace(text[0:3], a)

#   elif text[0] in capitol:
#     text=text.title()
#     if "-" in text:
#       text=text.split("-")
#     elif "_" in text:
#       text=text.split("_")
#     elif "-" and "_" in text:
#       text=text.split("_" and "_")
#       text="".join(text)
#     text="".join(text)

  
#   return text



# print(to_camel_case('a-Cat_Is-cute'))


def to_camel_case(text):
  capitol=['A','B','C','D','E','F','G','H','I','K','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

  if text=='':
    return ''

  if text[0] not in capitol:
    text=text.title()
    if "-" in text:
      text=text.split("-")
      text="".join(text)
      if "_" in text:
        text=text.split("_")
        text="".join(text)
    elif "_" in text:
      text=text.split("_")
      text="".join(text)
    a=text[0].lower()
    print(a)
    print(text)
    text="".join(text)
    text=text.replace(text[0], a)

  elif text[0] in capitol:
    text=text.title()
    if "-" in text:
      text=text.split("-")
      text="".join(text)
      if "_" in text:
        text=text.split("_")
        text="".join(text)
    elif "_" in text:
      text=text.split("_")
    elif "-" and "_" in text:
      text=text.split("_" and "_")
      text="".join(text)
    text="".join(text)

  
  return text



print(to_camel_case('The_stealth-warrior'))