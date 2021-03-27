# def duplicate_count(text):
#     count=0
#     for i, let in enumerate(text):
#         let=let.lower()
#         while i<len(text)-1:
#             print(i)
#             if let == let[i]:
#                 count+=1
#     return count
# print(duplicate_count("abba"))


def duplicate_count(text):
    text_two=text
    dupes=""
    for char in text:
      if char in text_two:
        dupes+=char
    return len(dupes)
print(duplicate_count("abba"))