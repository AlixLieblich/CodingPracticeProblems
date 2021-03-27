# def gimme(input_array):
#     print(input_array.sort(key=len))
#     if input_array==[]:
#         return[]
#     dup_arr=input_array
#     l=sorted(dup_arr)
#     mid=l[1]
#     for num in input_array:
#         if num==mid:
#             print(num)
#             num_i=input_array.index(num)
#     return num_i
# print(gimme(["howsy", "rar", "ajdaiaie"]))


list=["howsy", "rar", "ajdaiaie"]
print(sorted(list, key=len))


