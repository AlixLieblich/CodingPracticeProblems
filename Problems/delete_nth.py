def delete_nth(order,max_e):
    allowed=[]
    for pics in order:
        substring=pics
        if pics not in allowed:
            if allowed.count(pics) < max_e:
                allowed.append(pics)
                print(f"appended {substring} for not in")
        elif pics in allowed:
            print(f"counts of {substring}: ")
            print(allowed.count(pics))
            if allowed.count(pics) < max_e:
                allowed.append(pics)
    return allowed
print(delete_nth([1,1,3,3,7,2,2,2,2], 3))