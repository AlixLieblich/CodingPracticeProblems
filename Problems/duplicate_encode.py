def duplicate_encode(word):
    new_string=""
    for char in word:
        if word.count(char)>1:
            new_string+=(")")
        if word.count(char)<=1:
            new_string+=("(")
    return new_string
print(duplicate_encode("(())())"))