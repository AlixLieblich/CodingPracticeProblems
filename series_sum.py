
def series_sum(n):
    if n==0:
        return "0.00"
    j=1
    strng=1.00
    while j<n:
        strng+=(0.24*(n-1))
        j+=n
    return str(strng)
print(series_sum(3))