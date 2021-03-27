
def narcissistic( value ):
    value=str(value)
    power=len(value)
    total=0
    for num in value:
        num=int(num)
        powered=(num**power)
        total+=powered
    value=int(value)
    if total!=value:
      return False
    elif total ==value:
      return True
print(narcissistic(371))