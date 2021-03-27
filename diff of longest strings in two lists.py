def mxdiflg(a1, a2):
    short_a1, short_a2="",""
    i=0
    while i<len(a1):
        if len(a1[i])>len(short_a1):
            short_a1+=(a1[i])
        i+=1
    print(short_a1)    
    i=0
    while i<len(a2):
        if len(a2[i])>len(short_a2):
            short_a2+=(a2[i])
        i+=1
    answer= max(len(short_a1), len(short_a2))-min(len(short_a1),len(short_a2))
    return answer
print(mxdiflg(["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"],["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]))



def mxdiflg(a1, a2):
    short_a1, short_a2=[],[]
    i=0
    while i<len(a1):
        if len(a1[i])>len(short_a1):
            short_a1+=[]
            short_a1+=(a1[i])
            print(short_a1)
        i+=1
    short_a1=''.join(short_a1)
    # print(short_a1)    
    i=0
    while i<len(a2):
        if len(a2[i])>len(short_a2):
            short_a2+=[]
            short_a2+=(a2[i])
        i+=1
    short_a2=''.join(short_a2)
    # print(short_a2)
    # answer= max(len(short_a1), len(short_a2))-min(len(short_a1),len(short_a2))
    shortest=max(short_a1,short_a2)
    print(shortest)
print(mxdiflg(["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"],["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]))