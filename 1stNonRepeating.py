from collections import Counter
name = "Guru Rahul"
name = name.lower().replace(" ","")
count = Counter(name.strip())
print(count)
letters =[]
for i in name:
    if count[i] ==1:
        letters.append(i)
print(letters[0])