from collections import Counter
s=input('enter word')
a=input('emter anagram')
print(Counter(s))
if Counter(s)==Counter(a):
    print("true")
else:
    print('false')
                   
 