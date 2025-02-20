from collections import Counter
word ="malayalam"
word = word.lower()
word = word.replace(" ","")
check = 0
count = Counter(word)
for i in count.values():
    if i%2 !=0:
        check = check +1
if check >1:
    print("The word is not a Palindrome")
else:
    print("The word is a Palindrome")