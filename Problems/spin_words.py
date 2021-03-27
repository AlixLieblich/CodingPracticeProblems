def spin_words(sentence):
    print()
    spun=[]
    sentence=sentence.split(" ")
    print(sentence)
    for words in sentence:
        if len(words)<5:
            spun.append(str(words))
        if len(words)>=5:
            spun_words=words[::-1]
            spun.append(str(spun_words))
    spun=' '.join(spun)
    return spun

print(spin_words("If multiple interviews are scheduled, our admissions team will be in touch to consolidate. Thank you!" ))
# list1 = ['g','e','e','k', 's']  
# print("".join(list1)) 
