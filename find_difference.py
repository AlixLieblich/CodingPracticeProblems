#find the differnce of cub a and cube b


def find_difference(a, b):
    cube_a=(a[0]*a[1]*a[2])
    cube_b=(b[0]*b[1]*b[2])
    dif=max(cube_a,cube_b)-min(cube_a,cube_b)
    return dif
a=find_difference([5, 25, 15], [29, 5, 14])
print(a)

# def find_difference(a, b):
#    return max(((a[0]*a[1]*a[2]),(b[0]*b[1]*b[2]))-min(a[0]*a[1]*a[2]),(b[0]*b[1]*b[2]))
# m=find_difference([3, 2, 5], [1, 4, 4])
# print(m)

def find_difference(a, b):
   return abs((a[0]*a[1]*a[2])-(b[0]*b[1]*b[2]))
m=find_difference([5, 25, 15], [29, 5, 14])
print(m)