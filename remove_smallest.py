def remove_smallest(numbers):
    if numbers==[]:
        return []
    smallest=9999999999
    answer=[]
    i=0
    while i<len(numbers):
        if numbers[i]<smallest:
            smallest=0
            smallest+=numbers[i]
        i+=1
    small_i=numbers.index(smallest)
    i=0
    while i<len(numbers):
        answer.append(numbers[i])
        i+=1
    answer.pop(small_i)
    return answer
    
print(remove_smallest([4, 2, 3, 4, 5, 1]))