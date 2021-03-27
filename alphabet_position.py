def alphabet_position(text):
    alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    strng=""
    for let in text:
        let=let.lower()
        if let in alpha:
            x= alpha.index(let)+1
            x=str(x)
            strng+=x
            strng+=" "
    return strng[:-1]
print(alphabet_position("The narwhal bacons at midnight."))
