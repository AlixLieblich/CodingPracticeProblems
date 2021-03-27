def longest_consec(strarr, k):
    lst=""
    print(strarr)
    longest=max(strarr, key=len)
    print(longest)
    longest_i=strarr.index(longest)
    # k_lst=[]
    # l=0
    # while l<=k:
    #     k_lst.append(l)
    #     l+=1
    #     print(l)
    # print(k_lst)
    m=1
    while m<k:
        lst+=(strarr[longest_i+m])
        m+=1
    return longest+lst
print(longest_consec(['wlwsasphmxx', 'owiaxujylentrklctozmymu', 'wpgozvxxiu'],2))
