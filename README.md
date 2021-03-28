## 👩‍💻 Coding Challenges Practice 👩‍💻 

### 💻 Overview 💻 

An assortment of coding challenges solved from CodeWars.com up to rank Kyu 5. 70 + coding challenges completed to date!

## 💖 Example Problem ✨

```python

# An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
# Implement a function that determines whether a string that contains only letters is an isogram. 
# Assume the empty string is an isogram. Ignore letter case.

#define the function with parameter string
# for each char in string:
#   if used only once:
#      then True
#   if used more than once:
#        then False

def is_isogram(string):
  string=string.lower()
  char_set = [False] * 128
  for i in range(0, len(string)):
    val=ord(string[i])
    if char_set[val]:
      return False
    char_set[val]=True
  return True
print(is_isogram("isogram"))
```
