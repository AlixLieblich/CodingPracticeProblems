def validate_pin(pin):
    pin="".join(num for num in pin if num.isnumeric())
    print(pin)
    for num in pin:
      if num
    if len(pin)<4:
        return False
    elif len(pin)>6:
        return False
    elif len(pin)==4:
        return True
    elif len(pin)==6:
        return True
    elif len(pin)==5:
        return False
print(validate_pin("-1634"))